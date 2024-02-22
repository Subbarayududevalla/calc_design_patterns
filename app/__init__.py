class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")
        app = App()
        app.main_loop()

    def main_loop(self):
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            else:
                self.handle_command(user_input)

    def handle_command(self, command_name):
        if command_name in self.command_handler.commands:
            self.command_handler.execute_command(command_name)
        else:
            print(f"No such command: {command_name}")
