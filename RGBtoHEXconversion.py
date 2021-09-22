def rgb(r, g, b):
    def range(num):
        if num <= 0:return '00'
        elif num > 255:return 'FF'
        else: return "{00:X}".format(num)
    red=range(r)
    green=range(g)
    blue=range(b)
    return red.zfill(2)+green.zfill(2)+blue.zfill(2)