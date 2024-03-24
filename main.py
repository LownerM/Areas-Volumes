import time
def volouarea():
    print("Área [1], Volume[2]")
    global av
    av = int(input("Qual é o serviço que deseja?: "))
def questao1():
    print("Quadrado [1], Retângulo [2], Paralelogramo [3], Triângulo [4], Círculo [5]")
    global fg
    fg = int(input("Qual é a figura geométrica desejada?: "))
def questao2():
    print("Cubo [1], Paralelepípedo Retângulo [2], Cilindro [4]")
    global fgv
    fgv = int(input("Qual é a figura geométrica desejada?: "))
def area():
    questao1()
    if fg == 1:
        lq = float(input("Qual é o comprimento do lado do quadrado: "))
        aq = lq**2
        print(f"A área do quadrado é {aq} cm^2")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
    elif fg == 2:
        br = float(input("Qual é o comprimento da base do retângulo?: "))
        time.sleep(0.3)
        alr = float(input("Qual é o comprimento da altura do retângulo?: "))
        ar = br * alr
        print(f"A área do retângulo é {ar} cm^2")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
    elif fg == 3:
        bp = float(input("Qual é o comprimento da base do paralelogramo?: "))
        alp = float(input("Qual é o comprimento da altura relativa á base?: "))
        ap = bp * alp
        print(f"A área do paralelogramo é {ap} cm^2")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
    elif fg == 4:
        bt = float(input("Qual é o comprimento da base do triângulo: "))
        alt = float(input("Qual é o comprimento da altura relativa á base?: "))
        at = (bt * alt)/2
        print(f"A área do triângulo é {at} cm^2")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
    elif fg == 5:
        rc = float(input("Qual é o raio do círculo: "))
        rquadrado = rc**2
        ac = round((rquadrado*3.1416),2)
        print(f"A área do circulo é {ac} cm^2")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
def volume():
    questao2()
    if fgv == 1:
        lc = float(input("Qual é o comprimento do lado do cubo?: "))
        vtc = lc**3
        print(f"O volume do seu cubo são {vtc} cm^3")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
    if fgv == 2:
        lMr = float(input("Qual é o comprimento do lado maior do retângulo?: "))
        lmr = float(input("Qual é o comprimento do lado menor do retângulo?: "))
        car = float(input("Qual é o comprimento da altura do retângulo?: "))
        vr = lmr * lMr * car
        print(f"O volume do seu retângulo são {vr} cm^3")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
    if fgv == 3:
        rc = float(input("Qual é o raio do cilindro?: "))
        ac = float(input("Qual é a altura do cilindro?: "))
        rcquadrado = rc**2
        ab = rcquadrado * 3.1416
        vc = ab * ac
        print(f"O volume do seu cubo são {vc} cm^3")
        time.sleep(0.5)
        refazer = input("Deseja utilizar denovo o programa?(S/N): ")
        if refazer == 'S' or 's' or 'Sim' or 'sim':
            time.sleep(0.6)
            volouarea()
            if av == 1:
                area()
            elif av == 2:
                volume()
        else:
            print("Até á próxima!😊")
volouarea()
if av == 1:
    area()
elif av == 2:
    volume()
