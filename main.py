from manager.conversation_manager import ConversationManager

if __name__ == '__main__':
    manager = ConversationManager()
    

    print(manager.handle_input("I want to book a flight"))
    print(manager.handle_input("from NYC"))
    print(manager.handle_input("to LA"))
    print(manager.handle_input("on 2024-11-10"))