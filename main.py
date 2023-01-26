def flat_list(l):
    # input nested list is stored in l
    # Insert Code below
    sdl=[]
    for items in l:
        for i in items:
            sdl.append(i)
    # Insert Code Above
    # Return single-dimension list.
    return sdl
