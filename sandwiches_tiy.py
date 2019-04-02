def sandwiches(*components):
    print("You ordered a sandwich with the following: ")
    for component in components:
        print("\t" + component)

sandwiches('ham', 'swiss cheese', 'pickles')
sandwiches('tuna salad')
sandwiches('turkey', 'pepperjack cheese')