import requests # importando framework
import pandas as pd # importando framework
import collections

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil' 

r = requests.get(url, verify=False) # solicitando uma requisição e puxando a base de dados 

r.text

r_text = r.text
r_text = r.text.replace('\\r\n', '')                
r_text = r.text.replace('"\r\n}', '')
r_text = r.text.replace('{\r\n "html": "',  '')     #tratando a base de dados 
df = pd.read_html(r_text)                    

type(df)
type(df[0])    # Analisando o tipo de dado e modificando 

df=df[0].copy()      

df
df.columns

new_columns = df.columns
new_columns = list (i.replace('\\r\\n', '')for i in new_columns)
new_columns
df.columns = new_columns  

df[df['Bola1'] == df['Bola1']] # Tratando as colunas que estavam com espaço e vieram nulas

nr_pop = list(range(1,26))

nr_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

nr_impares = [1, 3 ,5 ,7 ,9 ,11 ,13 ,15 ,17 ,19 ,21 ,23 , 25]    # Criando vetores que vão receber o numeros pares , impares e primos  

nr_primos = [2 , 5 , 7 , 11, 13 ,17 , 19 ,23 , 25]

comb = []  # vetor vazio aonde ira receber todas as probabilidades de primos , pares e impares
V_1 = 0
V_2 = 0
V_3 = 0
V_4 = 0
V_5 = 0
V_6 = 0
V_7 = 0
V_8 = 0      
V_9 = 0
V_10 = 0
V_11 = 0
V_12 = 0                             # vetores que irão reprecentar  o numero de bolas 
V_13 = 0
V_14 = 0
V_15 = 0                                                  
V_16 = 0
V_17 = 0
V_18 = 0
V_19 = 0
V_20 = 0
V_21 = 0
V_22 = 0
V_23 = 0
V_24 = 0
V_25 = 0


lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8',
              'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']  # quatidades de bola por jogo 









for index, row in df.iterrows():
    v_pares   = 0
    v_impares = 0
    v_primos  = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            v_pares   += 1
        if row[campo] in nr_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos  += 1    
        if row[campo]  == 1:
            V_1 +=1
        if row[campo]  == 2:
            V_2 +=1
        if row[campo]  == 3:
            V_3 +=1
        if row[campo]  == 4:
            V_4 +=1
        if row[campo]  == 5:
            V_5 +=1 
        if row[campo]  == 6:
            V_6 +=1
        if row[campo]  == 7:
            V_7 +=1
        if row[campo]  == 8:
            V_8 +=1
        if row[campo]  == 9:
            V_9 +=1
        if row[campo]  == 10:
            V_10 +=1
        if row[campo]  == 11:
            V_11 +=1
        if row[campo]  == 12:
            V_12 +=1
        if row[campo]  == 13:
            V_13 +=1
        if row[campo]  == 14:
            V_14 +=1
        if row[campo]  == 15:
            V_15 +=1
        if row[campo]  == 16:
            V_16 +=1
        if row[campo]  == 17:
            V_17 +=1
        if row[campo]  == 18:
            V_18 +=1
        if row[campo]  == 19:
            V_19 +=1
        if row[campo]  == 20:
            V_20 +=1
        if row[campo]  == 21:
            V_21 +=1
        if row[campo]  == 22:
            V_22 +=1
        if row[campo]  == 23:
            V_23 +=1
        if row[campo]  == 24:
            V_24 +=1
        if row[campo]  == 25:
            V_25 +=1
    comb.append(str(v_pares)+ 'p-' + str(v_impares) + 'i-' + str(v_primos) + 'np-') 


    freq_nr = [[1,V_1],
               [2,V_2],
               [3,V_3],
               [4,V_4],
               [5,V_5],
               [6,V_6],
               [7,V_7],
               [8,V_8],
               [9,V_9],
               [10,V_10],
               [11,V_11],
               [12,V_12],
               [13,V_13],
               [14,V_14],
               [15,V_15],
               [16,V_16],
               [17,V_17],
               [18,V_18],
               [19,V_19],
               [20,V_20],
               [21,V_21],
               [22,V_22],
               [23,V_23],
               [24,V_24],
               [25,V_25]] 

freq_nr .sort(key=lambda tup: tup[1])

freq_nr [0]

freq_nr[-1]


counter = collections.Counter(comb)
resultado = pd.DataFrame(counter.items(), columns=['Combinacao', 'Frequencia'])
resultado ['p_freq'] = resultado['Frequencia']/resultado['Frequencia'].sum()          
resultado = resultado.sort_values(by= 'p_freq')                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                                                                                         