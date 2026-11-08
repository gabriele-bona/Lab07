import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdowns(self):
        """Popola i menu a tendina della View con i dati letti dal Model."""
        # 1. Popola Biblioteche
        biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.clear()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))
        self._view.dd_biblioteca.value = "Nessun filtro"
        # 2. Popola Generi
        generi = self._model.get_generi()
        self._view.dd_genere.options.clear()
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(g))
        self._view.dd_genere.value = "Nessun filtro"

    # CALLBACKS DROPDOWN
    def handler_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value

    def handler_genere(self, e):
        self.genere_selezionato = self._view.dd_genere.value

    # AZIONE: MOSTRA LIBRI
    def handler_mostra(self, e):
        self._view.lst_libri.controls.clear()
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if not libri:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati.")
            self._view.update()
            return
        for libro in libri:
            self._view.lst_libri.controls.append(ft.Text(value=str(libro)))
        self._view.update()