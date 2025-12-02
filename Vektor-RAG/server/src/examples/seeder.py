"""Data RAG Example - Complete setup in one file"""

import os
from core.document import Document
from core.rag_service import RAGService
from core.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from core.vector_stores.chroma_vector_store import ChromaVectorStore

# Example documents
DOCUMENTS = [
    Document(
        title="Grundlagen der Drachenpflege",
        content="Die richtige Pflege von Drachen erfordert täglich frisches Fleisch, ausreichend Bewegung und regelmäßige Fellpflege. Feuerdrachen benötigen zusätzlich vulkanische Steine zur Temperaturregulierung. Wichtig: Niemals bei Vollmond füttern!"
    ),
    Document(
        title="Drachenarten und ihre Eigenschaften",
        content="Eisdrachen sind friedlich aber territorial. Feuerdrachen sind loyal aber temperamentvoll. Walddrachen sind scheu und bevorzugen vegetarische Kost. Wasserdrachen können bis zu 3 Stunden unter Wasser bleiben und sind ausgezeichnete Schwimmer."
    ),
    Document(
        title="Sicherheitsmaßnahmen im Umgang mit Drachen",
        content="Trage immer feuerfeste Kleidung. Nähere dich niemals von hinten. Verwende beruhigende Töne und langsame Bewegungen. Bei aggressivem Verhalten sofort Schutzposition einnehmen. Notfallausrüstung: Löschpulver, Beruhigungstränke, Schutzschild."
    ),
    Document(
        title="Drachentraining für Anfänger",
        content="Beginne mit einfachen Kommandos: Sitz, Bleib, Komm. Belohne gutes Verhalten mit Lieblingsleckerlis. Flugtraining erst nach 6 Monaten Grundgehorsam. Verwende positive Verstärkung, niemals Gewalt. Trainingszeit: maximal 30 Minuten am Stück."
    ),
    Document(
        title="Drachenkrankheiten und Heilmittel",
        content="Schuppenfäule: Mit Drachenminze-Salbe behandeln. Flügellahme: Ruhe und warme Umschläge. Feuermangel: Schwefelreiches Futter verabreichen. Melancholie: Gesellschaft anderer Drachen oder längere Flüge. Bei Symptomen sofort Drachenheiler kontaktieren."
    ),
    Document(
        title="Drachenzucht und Nachwuchs",
        content="Brutzeit: 3-4 Monate je nach Art. Eier benötigen konstante Temperatur von 45°C. Schlüpflinge sind blind und hilflos. Erste Nahrung: warme Drachenmilch. Flugfähigkeit nach 2-3 Monaten. Geschlechtsreife nach 50-100 Jahren je nach Drachenart."
    ),
    Document(
        title="Rechtliche Bestimmungen für Drachenhalter",
        content="Drachen müssen bei der Magischen Behörde registriert werden. Haftpflichtversicherung ist Pflicht. Flüge nur in ausgewiesenen Gebieten. Lärmschutzverordnung beachten (Gebrüll nach 22 Uhr verboten). Jährliche Gesundheitsprüfung durch zertifizierten Drachenheiler."
    ),
    Document(
        title="Drachenpsychologie verstehen",
        content="Drachen sind hochintelligente, emotionale Wesen. Sie bilden starke Bindungen zu ihren Betreuern. Langeweile führt zu destruktivem Verhalten. Beschäftigung durch Rätsel, Schatzsuche oder Flugspiele. Respektiere ihre Würde und Unabhängigkeit."
    )
]


def main():
    # Setup RAG
    embedder = SentenceTransformerEmbedder("BAAI/bge-m3")
    vector_store = ChromaVectorStore(os.getenv("VECTOR_COLLECTION", "rag"))
    rag_service = RAGService(embedder, vector_store)

    # Load documents
    for doc in DOCUMENTS:
        rag_service.add_document(doc.title, doc.content)
    print("Dokumente erfolgreich geladen")

    # Start server
    import core.__main__ as core_main
    setattr(core_main, "rag_service", rag_service)
    core_main.main()

if __name__ == "__main__":
    main()
