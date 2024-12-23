'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. 
O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, 
organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''


class TaskHandler:
    def execute(self) -> bool:
        self.__conect_api()
        task = Task()
        task.create_task()
        task.update_task()
        task.remove_task()
        self.__send_notification()
        report = Report()
        report.generate_report()
        report.send_report()
        return True

    def __conect_api() -> None:
        print("Connect to API.....")

    def __send_notification() -> None:
        print("Send notification.....")


class Task:
    def create_task() -> None:
        print("Task created.....")

    def update_task() -> None:
        print("Task updated.....")

    def remove_task() -> None:
        print("Task removed.....")


class Report:
    def generate_report() -> None:
        print("Generate report.....")

    def send_report() -> None:
        print("Send report.....")
