from concurrent.futures import ProcessPoolExecutor, as_completed

# Function to check if a position is within a specified range
def is_within_range(item, h_bounds: tuple, v_bounds: tuple):
    assert item.pos is not None
    return h_bounds[0] <= item.pos.x <= h_bounds[1] & v_bounds[0] <= item.pos.y <= v_bounds[1]

# Parallelizing the check using ProcessPoolExecutor
def get_entities_in_camera(items: list, h_bounds: tuple, v_bounds: tuple):
    results = []
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(is_within_range, item, h_bounds, v_bounds): item for item in items}
        
        for future in as_completed(futures):
            item = futures[future]
            try:
                result = future.result()
                results.append((item, result))
            except Exception as e:
                print(f"Error processing item {item}: {e}")
    
    return results
