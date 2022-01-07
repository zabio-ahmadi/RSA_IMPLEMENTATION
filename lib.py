def exp_rapide(x,pow,n): 
    result=1 
    while pow!=0: 
        if pow%2==1:
            result = (result * x) % n
        pow//=2 
        x = (x * x) % n 
    return result


def calc_p_q(n):
    nb_premier = n
    facteur  = 2
    while facteur * facteur < nb_premier:
        while nb_premier % facteur == 0:
            nb_premier = nb_premier / facteur
        facteur += 1 
    return int(n/nb_premier), int(nb_premier)


def calc_z(n):
    p_q = []
    p_q = calc_p_q(n)
    return (p_q[0] -1) *(p_q[1] - 1)


def euclide_etendu(dividende, diviseur):
    #initialisation
    x = 1 #x0
    v = 1 #y1
    y = 0 #y0
    u = 0 #x1
    diviseur_pour_inverse = diviseur #permettra de calculer l'inverse modulaire
    #euclide simple
    while diviseur != 0:
        quotient = dividende // diviseur # // : floor division 
        reste = dividende % diviseur
        dividende = diviseur
        diviseur = reste
    #-----------------------------------
    #euclide etendu
        m = u-quotient*x
        n = v-quotient*y
        u = x
        v = y
        x = m
        y = n
    #------------------------------------
    
    # return inverse modulaire
    if diviseur != 0:
        return (v ,u, "NULL")
    else:
        return (v ,u, v % diviseur_pour_inverse)


def calc_private_key(public_key, n):

    z = calc_z(n)
    return euclide_etendu(z, public_key)[1]


def decode_by_private_key(key, n, message_list):
    decoded_message_by_private_key = list() # message in iteger form 
    
    for mgs in message_list:
        decoded_message_by_private_key.append(exp_rapide(mgs,key,n))
    
    return decoded_message_by_private_key

def decode_raw_data(raw_message_list):
    decoded_message = ""
    for msg in raw_message_list:
        decoded_message += msg.to_bytes(len(str(msg)), 'little').decode('utf8')
    
    return decoded_message