import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_cross_product_with_area(vector_a, vector_b):
    # Ensure the vectors are in 3D (by adding a z-component of 0)
    vector_a_3d = np.array([vector_a[0], vector_a[1], 0])  # A vector in XY plane
    vector_b_3d = np.array([vector_b[0], vector_b[1], 0])  # B vector in XY plane

    # Calculate the cross product (this will give a vector in the Z direction)
    cross_product = np.cross(vector_a_3d, vector_b_3d)

    # Force the cross product to point upwards (positive Z-direction)
    if cross_product[2] < 0:  # Check the Z-component of the cross product
        cross_product = -cross_product  # Flip the cross product to point upwards

    # Create the figure and the 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the origin
    origin = np.array([0, 0, 0])

    # Plot vectors A and B as arrows (only 2D parts)
    ax.quiver(origin[0], origin[1], origin[2], vector_a_3d[0], vector_a_3d[1], vector_a_3d[2], color='r',
              label='Vector A', linewidth=3)
    ax.quiver(origin[0], origin[1], origin[2], vector_b_3d[0], vector_b_3d[1], vector_b_3d[2], color='b',
              label='Vector B', linewidth=3)

    # Plot the cross product vector as an arrow (cross product is purely in Z direction)
    ax.quiver(origin[0], origin[1], origin[2], 0, 0, cross_product[2], color='g', label='Cross Product', linewidth=3)

    # Create the parallelogram using the vectors
    x_vals = [origin[0], vector_a_3d[0], vector_a_3d[0] + vector_b_3d[0], vector_b_3d[0], origin[0]]
    y_vals = [origin[1], vector_a_3d[1], vector_a_3d[1] + vector_b_3d[1], vector_b_3d[1], origin[1]]
    z_vals = [origin[2], vector_a_3d[2], vector_a_3d[2] + vector_b_3d[2], vector_b_3d[2], origin[2]]

    ax.plot_trisurf(x_vals, y_vals, z_vals, color='orange', alpha=0.5, edgecolors='black', label='Area (Parallelogram)')

    # Setting the labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cross Product and Parallelogram Area')

    # Set axis limits for better visualization
    ax.set_xlim([-2, 5])
    ax.set_ylim([-2, 5])
    ax.set_zlim([0, 5])

    # Set the viewing angle
    ax.view_init(elev=40, azim=60)  # Adjust the camera view (elevation and azimuth)

    # Show the legend
    ax.legend()

    # Display the plot
    plt.show()


# Function to take input for vectors A and B
def get_vector_input(name):
    x = float(input(f"Enter the x-component of {name}: "))
    y = float(input(f"Enter the y-component of {name}: "))
    return np.array([x, y])


# Interactive loop for adjusting vectors
def interactive_plot():
    print("Please enter the components for Vector A and Vector B.")

    vector_a = get_vector_input('Vector A')
    vector_b = get_vector_input('Vector B')

    plot_cross_product_with_area(vector_a, vector_b)


# Call the interactive plot function
interactive_plot()
