@qgsfunction(args='auto', group='Custom')
def dynamic_row_number(feature, parent):
    """
    Restituisce un numero progressivo per ogni elemento.

    Funzionamento:
    - Incrementa un contatore globale ogni volta che viene chiamata.
    - Restituisce il valore corrente del contatore.

    Parametri:
    - feature: L'elemento corrente (non utilizzato per il conteggio).
    - parent: Il contesto del motore di espressioni (non utilizzato direttamente).

    Ritorna:
    - Un numero intero progressivo.
    """
    counter_name = "custom_row_counter"
    current_value = QgsExpressionContextUtils.globalScope().variable(counter_name)
    current_value = int(current_value) + 1 if current_value is not None else 1
    QgsExpressionContextUtils.setGlobalVariable(counter_name, str(current_value))
    return current_value

def reset_counter():
    """
    Resetta il contatore globale del numero progressivo.

    Utilizzo:
    - Chiamare questa funzione prima di iniziare un nuovo ciclo di numerazione
      (ad esempio, prima di generare un report).
    """
    QgsExpressionContextUtils.setGlobalVariable("custom_row_counter", "0")

    