names = [
    'Zena Engebretson',
    'Celinda Bonavita',
    'Lucio Persing', 
    'Juliette Severs',
    'Kelly Humfeld',
    'Franklyn Hornick',
    'Newton Novello',
    'Sammy Sheppard',
    'Polly Bly',
    'Genevive Finch',
    'Teodora Etheredge',
    'Sunshine Mcniff',
    'Vicki Tito',
    'Clemmie Birkhead',
    'Mohammad Luz',
    'Lissette Mellon',
    'Mozell Mcduffie',
    'Devin Bolten',
    'Bridget Pottorff'
]

with open('output.txt', 'w') as txt_file:
    for name in names:
        txt_file.write(name + '\n')
