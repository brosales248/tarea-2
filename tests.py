from smart_editor import SmartEditor

def test_all():
    ed = SmartEditor()

    ed.write("Hola")
    assert ed.get_text() == "Hola"

    ed.delete(2)
    assert ed.get_text() == "Ho"


    ed.undo()
    assert ed.get_text() == "Hola"


    ed.undo()
    assert ed.get_text() == ""


    ed.redo()
    assert ed.get_text() == "Hola"

    print("Todo OK")

if __name__ == "__main__":
    test_all()