import pandas as pd
import numpy as np
import open3d as o3d

def create_aggregated_point_cloud(values, shapes):
  all_points = []

  for value, shape in zip(values, shapes):
    
    range_image = np.array(value)
    range_image_reshaped = range_image.reshape(shape)
    ranges = range_image_reshaped[..., 0]
    azimuths = range_image_reshaped[..., 1]
    elevations = range_image_reshaped[..., 2]
    x = ranges * np.cos(elevations) * np.sin(azimuths)
    y = ranges * np.cos(elevations) * np.cos(azimuths)
    z = ranges * np.sin(elevations)
    points = np.stack((x, y, z), axis=-1).reshape(-1, 3)
    all_points.append(points)
  all_points = np.vstack(all_points)
  point_cloud = o3d.geometry.PointCloud()
  point_cloud.points = o3d.utility.Vector3dVector(all_points)
  o3d.visualization.draw_geometries([point_cloud])
parquet_file_path = '/Users/sid/Desktop/Personel/SJSU/PP CP Research/Data/training_lidar_10017090168044687777_6380_000_6400_000.parquet'

df = pd.read_parquet(parquet_file_path)
range_image_return1_values = df['[LiDARComponent].range_image_return1.values']
range_image_return1_shape = df['[LiDARComponent].range_image_return1.shape']
create_aggregated_point_cloud(range_image_return1_values, range_image_return1_shape)
