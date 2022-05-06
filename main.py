        # obtendo as unidades
        a = c_de.get()
        b = c_para.get()

        #   obtendo o número
        numero_para_converter = float(e_numero.get())

        dist = unidade_para.index(b) - unidade_de.index(a)

        # contas

        # mutiplicação
        if unidade_para.index(a) <= unidade_de.index(b):

            distancia = unidade_para.index(b) - unidade_de.index(a)
            resultado = numero_para_converter * (10**distancia)

            l_resultado['text'] = resultado

        else:
            distancia = unidade_de.index(a) - unidade_para.index(b)
            resultado = numero_para_converter * (10**distancia)

        # divisão
        if unidade_para.index(a) > unidade_de.index(b):

            if unidade_para.index(a) <= unidade_de.index(b):

                distancia = unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter / (10**distancia)

                l_resultado['text'] = resultado

            else:

                distancia = unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter / (10**distancia)
                l_resultado['text'] = resultado

        print(a, b, numero_para_converter)

    # crinado Label, Botão, entrada

    l_info = Label(frame_direita, text='Digite o numero', width=16, height=2, padx=0,
                   pady=3, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
    l_info.place(x=0, y=110)

    e_numero = Entry(frame_direita, width=9, font=(
        'Ivy 15 bold'), justify='center', relief=SOLID)
    e_numero.place(x=0, y=150)

    b_calcular = Button(frame_direita, command=calcular,  text='Calcular', width=8, height=1, relief='raised',
                        overrelief='ridge', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor2)
    b_calcular.place(x=115, y=150)

    l_resultado = Label(frame_direita, text='', width=12, height=1, padx=0,
                        pady=3, relief='groove', anchor='center', font=('Ivy 18 bold'), bg=cor2, fg=cor1)
    l_resultado.place(x=0, y=200)

# ----------------------------------------- Configurando Frame Direita -------------------------------------

l_unidade_nome = Label(frame_direita, text='---', width=16, height=2, padx=0,
                       relief='groove', anchor='center', font=('Ivyy 15 bold'), bg=cor2, fg=cor3)
l_unidade_nome.place(x=0, y=0)

l_de = Label(frame_direita, text='De', height=1, padx=3, relief='groove',
             anchor='center', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
l_de.place(x=10, y=70)
c_de = ttk.Combobox(frame_direita, width=5,
                    justify=('center'), font=('Ivy 8 bold'))
c_de.place(x=38, y=70)

l_para = Label(frame_direita, text='Para', height=1, padx=3, relief='groove',
               anchor='center', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
l_para.place(x=100, y=70)
c_para = ttk.Combobox(frame_direita, width=5,
                      justify=('center'), font=('Ivy 8 bold'))
c_para.place(x=140, y=70)
