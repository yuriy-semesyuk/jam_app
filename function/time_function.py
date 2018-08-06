

def time_int(time_str):
    h = ""
    m = ""
    t = 0
    for n in time_str:
        if n != ":" and t == 0:
            h = h + n
        elif n == ":":
            t = + 1
        else:
            m = m + n
    return time_sec(int(h), int(m))


def time_sec(h, m):
    secund = (h * 3600) + (m * 60)
    return secund


def time_plus(time_reg, time_servis):
    time_long = (time_reg + time_servis)
    return time_all_sec(time_long)


def time_all_sec(sec):
    h = (sec - (sec % 3600)) / 3600
    m = (sec % 3600) / 60
    return time_norm(h, m)


def time_norm(h, m):
    hover = str(h)
    minets = None
    if m > 9:
        minets = str(m)
    else:
        minets = "0" + str(m)
    return hover + ":" + minets


def list_time(a, b):
    listes = []
    listes.append(a)
    while a != b:
        a = time_all_sec(time_int(a) + time_int("0:15"))
        if a != b:
            listes.append(a)
    return listes


def time_setvic(a, b):
    time_fini_sec = time_int(a) + time_int(b)
    time_fini = time_all_sec(time_fini_sec)
    return time_fini



def for_type_service(servis):
    list_s = []
    y = ""
    for i in servis:
        if i != "/":
            y = y + i
        else:
            list_s.append(y)
            y = ""
    return list_s

def cont(a):
    return a+1





