import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="darkgrid")

def plot_data(list_epoch):
    data = []
    for epoch_info in list_epoch:
        weights = epoch_info['weights']
        data.append({'id': epoch_info['id'], 'error_norma': epoch_info['norm_error'], **{'weight_'+str(i): weights[i] for i in range(len(weights))}})

    df = pd.DataFrame(data)

    plt.figure(figsize=(20, 6))

    plt.subplot(1, 2, 1)
    for i in range(1, len(list_epoch[0]['weights'])):
        sns.lineplot(x='id', y='weight_'+str(i), data=df, label='Peso '+str(i), sort=False)
    plt.title('Cambios en los pesos en cada iteración')
    plt.xlabel('Época')
    plt.ylabel('Pesos')

    plt.subplot(1, 2, 2)
    sns.lineplot(x='id', y='error_norma', data=df, label='norma del error |e|', color='r', sort=False)
    plt.title('Norma del error en cada iteración')
    plt.xlabel('Época')
    plt.ylabel('Norma del error')

    plt.tight_layout()
    plt.show()