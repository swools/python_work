def make_sandwich(*sandwiches):
    print(f"\nThis sandwich contains the following ingredients...")
    for sandwich in sandwiches:
        print(f"- {sandwich}")
        
make_sandwich('lettuce')
make_sandwich('lettuce', 'tomato')
make_sandwich('lettuce', 'tomato', 'bacon')