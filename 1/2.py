for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            result = not (x or y or z ) == (not x and not y and not z)
            print("'not ({0} or {1} or {2} ) = (not {0}) and (not {1}) and (not {2})' is '{3}'".format(x, y, z, result))