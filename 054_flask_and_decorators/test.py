def im_inner():
    print("im inner")

    def im_outher():
        print("im outher")

    return im_outher


im_inner()()
