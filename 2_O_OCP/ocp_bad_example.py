'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para 
aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. 
Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a 
complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado
(Open Closed Principle). Utilizando do conceito do OCP, crie uma 
interface e classes que implementam a mesma para que, caso a clínica 
necessite de um novo tipo de exame, uma nova classe seja adicionada, 
implementando métodos de uma interface padrão para exames.

'''

from abc import ABC, abstractmethod


class Exame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self) -> None: pass

    @abstractmethod
    def verifica_condicoes_exame(self) -> None: pass


class BloodeExam(Exame):
    def verifica_condicoes_exame(self) -> None:
        print("Verify blood exam conditions.....")

    def aprovar_solicitacao_exame(self) -> None:
        print("Blood exam approved!")


class RayXExam(Exame):
    def verifica_condicoes_exame(self) -> None:
        print("Verify RayX exam conditions.....")

    def aprovar_solicitacao_exame(self) -> None:
        print("RayX exam approved!")


class AprovaExame:
    def __init__(self, exam: Exame) -> None:
        self.exam = exam

    def aprovar_solicitacao_exame(self) -> None:
        self.exam.verifica_condicoes_exame()
        self.exam.aprovar_solicitacao_exame()


print()
exame_sangue = BloodeExam()
aprovador = AprovaExame(exame_sangue)
aprovador.aprovar_solicitacao_exame()
print()
exame_raio_x = RayXExam()
aprovador = AprovaExame(exame_raio_x)
aprovador.aprovar_solicitacao_exame()
