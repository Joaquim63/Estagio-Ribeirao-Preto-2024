''' 
1 - Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
2 - Depois de alguns minutos, desligue o primeiro interruptor e ligue o segundo interruptor.
3 - Vá até a sala das lâmpadas.

Neste ponto, você pode identificar qual interruptor controla cada lâmpada da seguinte maneira:

- A lâmpada que está acesa deve ser controlada pelo segundo interruptor, que é o único interruptor que você deixou ligado.
- A lâmpada que está apagada e fria deve ser controlada pelo terceiro interruptor, que nunca foi ligado.
- A lâmpada que está apagada mas quente ao toque deve ser controlada pelo primeiro interruptor. Ela esquentou quando o primeiro interruptor estava ligado, e continuou quente mesmo depois de você desligá-lo.

OBS: 
a solução desse problema depende de interações físicas 
(como sentir o calor de uma lâmpada) que não podem ser
 representadas diretamente em um programa de computador.
 
'''

class Lamp:
    def __init__(self):
        self.state = 'off'

    def turn_on(self):
        self.state = 'on'

    def turn_off(self):
        if self.state == 'on':
            self.state = 'was on'
        else:
            self.state = 'off'

    def check_state(self):
        return self.state

# Cria as lâmpadas
lamp1 = Lamp()
lamp2 = Lamp()
lamp3 = Lamp()

# Ligue o primeiro interruptor (lamp1) e deixe-o ligado por alguns minutos
lamp1.turn_on()
# Depois de alguns minutos, desligue o primeiro interruptor (lamp1) e ligue o segundo interruptor (lamp2)
lamp1.turn_off()
lamp2.turn_on()

# Verifique o estado de cada lâmpada
print("Lamp 1: ", lamp1.check_state())
print("Lamp 2: ", lamp2.check_state())
print("Lamp 3: ", lamp3.check_state())
