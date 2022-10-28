class Target:
    """
    Target визначає доменно-спеціальний інтерфейс, який використовується кодом клієнта.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    Adaptee містить деяку корисну поведінку, але його інтерфейс несумісний
    з існуючим кодом клієнта. Адаптований потребує певної адаптації перед тим, як
    код клієнта може використовувати його.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    Адаптер робить інтерфейс Адаптованого сумісним з інтерфейсом Цілі
    інтерфейс через множинне успадкування.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    Код клієнта підтримує всі класи, які слідують інтерфейсу Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Клієнт: Я можу чудово працювати з цільовими об’єктами:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Клієнт: клас Adaptee має дивний інтерфейс. "
          "Бачите, я не розумію:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Клієнт: Але я можу працювати з ним через адаптер:")
    adapter = Adapter()
    client_code(adapter)
