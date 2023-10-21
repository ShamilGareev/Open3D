import open3d as o3d

# Load a point cloud from a file
pcd = o3d.io.read_point_cloud("bunny.pcd")

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])

# Basic operations on the point cloud
# Example: Downsample the point cloud
voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.02)
o3d.visualization.draw_geometries([voxel_down_pcd])

# Example: Compute normals for the point cloud
voxel_down_pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([voxel_down_pcd])

# Example: Segment the point cloud using RANSAC
inlier_cloud, outlier_cloud = voxel_down_pcd.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

# Example: Clustering the point cloud
clustering = voxel_down_pcd.cluster_dbscan(eps=0.02, min_points=10, print_progress=True)
for i, cluster in enumerate(clustering):
    cluster.paint_uniform_color([i / len(clustering), 0, 1 - i / len(clustering)])
o3d.visualization.draw_geometries(list(clustering))
