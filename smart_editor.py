from action_stack import ActionStack

class SmartEditor:
    def __init__(self):
        self._text = ""
        self._undo = ActionStack()
        self._redo = ActionStack()
        self._log = []

    def write(self, text):
        if not text.strip():
            raise ValueError("Texto vacío no permitido")

        self._text += text
        self._undo.push(("write", text))
        self._redo = ActionStack()
        self._log.append(f"write('{text}')")

    def delete(self, n):
        if n <= 0:
            raise ValueError("Número inválido")

        if n > len(self._text):
            raise ValueError("No puedes borrar más de lo existente")

        removed = self._text[-n:]
        self._text = self._text[:-n]

        self._undo.push(("delete", removed))
        self._redo = ActionStack()
        self._log.append(f"delete({n})")

    def undo(self):
        if self._undo.is_empty():
            raise Exception("Nada que deshacer")

        action, value = self._undo.pop()

        if action == "write":
            self._text = self._text[:-len(value)]
        elif action == "delete":
            self._text += value

        self._redo.push((action, value))
        self._log.append("undo()")

    def redo(self):
        if self._redo.is_empty():
            raise Exception("Nada que rehacer")

        action, value = self._redo.pop()

        if action == "write":
            self._text += value
        elif action == "delete":
            self._text = self._text[:-len(value)]

        self._undo.push((action, value))
        self._log.append("redo()")

    def get_text(self):
        return self._text

    def get_log(self):
        return self._log

    def length(self):
        return len(self._text)