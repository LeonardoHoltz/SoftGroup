import numpy as np
import pandas as pd

def create_point_cloud_plane(size, num_points):
    # Generate random x and y coordinates within the specified size
    x_coordinates = np.random.uniform(0, size, num_points)
    y_coordinates = np.random.uniform(0, size, num_points)

    # Z-coordinate for the plane (assuming it's flat)
    z_coordinate = 0.0

    # Set color values to 255.0 for each point
    colors = np.full((num_points, 3), 255.0)

    # Combine coordinates and colors into a single array
    point_cloud = np.column_stack((x_coordinates, y_coordinates, np.full(num_points, z_coordinate), colors))

    return point_cloud

def save_point_cloud_txt(point_cloud, filename):
    # Save the point cloud to a text file without a header
    np.savetxt(filename, point_cloud, fmt='%.6f %.6f %.6f %.1f %.1f %.1f', comments='', header='')

def point_cloud_to_dataframe(point_cloud):
    # Convert the point cloud to a Pandas DataFrame
    columns = ['x', 'y', 'z', 'r', 'g', 'b']
    df = pd.DataFrame(point_cloud, columns=columns)
    return df

if __name__ == "__main__":
    # Set the desired size and number of points
    plane_size = 30.0  # in meters
    num_points = 2000000

    # Create the point cloud
    point_cloud = create_point_cloud_plane(plane_size, num_points)

    # Save the point cloud to a text file without a header
    save_point_cloud_txt(point_cloud, 'point_cloud_plane.txt')

    # Convert point cloud to Pandas DataFrame
    df = point_cloud_to_dataframe(point_cloud)

    # Print the first few rows of the DataFrame
    print(df.head())