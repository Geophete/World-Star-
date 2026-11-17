from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class CampusApp(App):
    def build(self):
        self.notes = []
        main = BoxLayout(orientation='vertical', padding=15, spacing=10)

        main.add_widget(Label(text="WORLD STAR MOYENNE CAMPUS", font_size=22, bold=True, color=(0,0,0,1), size_hint_y=None, height=35))
        main.add_widget(Label(text="Par AGASSOUSSI Geophete - Cotonou", font_size=12, color=(0.3,0.3,0.3,1), size_hint_y=None, height=20))

        self.nom = TextInput(hint_text="Nom de l'etudiant", multiline=False, size_hint_y=None, height=45)
        self.matiere = TextInput(hint_text="Matiere (ex: Maths)", multiline=False, size_hint_y=None, height=45)
        self.note = TextInput(hint_text="Note sur 20 (ex: 15)", multiline=False, input_filter='float', size_hint_y=None, height=45)
        main.add_widget(self.nom)
        main.add_widget(self.matiere)
        main.add_widget(self.note)

        btn_add = Button(text="AJOUTER LA NOTE", background_color=(1,0.8,0,1), color=(0,0,0,1), size_hint_y=None, height=50)
        btn_add.bind(on_press=self.ajouter)
        main.add_widget(btn_add)

        self.liste = Label(text="Aucune note pour le moment", font_size=14)
        main.add_widget(self.liste)

        btn_calc = Button(text="CALCULER MA MOYENNE", background_color=(0,0,0,1), color=(1,0.8,0,1), size_hint_y=None, height=55)
        btn_calc.bind(on_press=self.calculer)
        main.add_widget(btn_calc)

        self.result = Label(text="", font_size=18, bold=True)
        main.add_widget(self.result)
        return main

    def ajouter(self, instance):
        try:
            n = float(self.note.text)
            if n < 0 or n > 20:
                self.result.text = "Note doit etre entre 0 et 20 !"
                return
            self.notes.append(n)
            self.liste.text = "Notes: " + ", ".join([str(x) for x in self.notes])
            self.note.text = ""
            self.result.text = ""
        except:
            self.result.text = "Tape seulement un chiffre !"

    def calculer(self, instance):
        if not self.notes:
            self.result.text = "Ajoute d'abord une note !"
            return
        moy = sum(self.notes) / len(self.notes)
        if moy >= 16:
            mention = "Tres Bien"
        elif moy >= 14:
            mention = "Bien"
        elif moy >= 12:
            mention = "Assez Bien"
        elif moy >= 10:
            mention = "Passable"
        else:
            mention = "Ajourne"
        self.result.text = f"{self.nom.text}\nMoyenne: {moy:.2f}/20\nMention: {mention}"

if __name__ == "__main__":
    CampusApp().run()
