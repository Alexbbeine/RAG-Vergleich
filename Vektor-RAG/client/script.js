const API_BASE = 'http://localhost:8000';

function showMessage(text, type = 'success') {
    const messages = document.getElementById('messages');
    const msg = document.createElement('div');
    msg.className = `message ${type}`;
    msg.textContent = text;
    messages.appendChild(msg);
    setTimeout(() => msg.remove(), 5000);
}

async function addDocument() {
    const title = document.getElementById('docTitle').value;
    const content = document.getElementById('docContent').value;

    if (!title || !content) {
        showMessage('Bitte füllen Sie sowohl Titel als auch Inhalt aus', 'error');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/documents`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, content })
        });

        const result = await response.json();

        if (result.status === 'added') {
            showMessage('Dokument erfolgreich hinzugefügt');
            document.getElementById('docTitle').value = '';
            document.getElementById('docContent').value = '';
            loadAllDocuments();
        } else if (result.status === 'exists') {
            showMessage('Dokument existiert bereits', 'error');
        } else {
            showMessage('Fehler beim Hinzufügen des Dokuments', 'error');
        }
    } catch (error) {
        showMessage('Fehler: ' + error.message, 'error');
    }
}

async function searchDocuments() {
    const query = document.getElementById('searchQuery').value;
    const numResults = parseInt(document.getElementById('numResults').value) || 5;

    if (!query) {
        showMessage('Bitte geben Sie eine Suchanfrage ein', 'error');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/search`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, n_results: numResults })
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const results = await response.json();

        if (!Array.isArray(results)) {
            throw new Error('Ungültige Antwort vom Server');
        }

        const container = document.getElementById('searchResults');
        container.innerHTML = '';

        if (results.length === 0) {
            container.innerHTML = '<p>Keine Ergebnisse gefunden</p>';
            return;
        }

        results.forEach(doc => {
            const div = document.createElement('div');
            div.className = 'document search-result';
            div.innerHTML = `
                <div class="document-title">${doc.title}</div>
                <div>${doc.content}</div>
                ${doc.distance ? `<small>Distanz: ${doc.distance.toFixed(3)}</small>` : ''}
            `;
            container.appendChild(div);
        });
    } catch (error) {
        showMessage('Suchfehler: ' + error.message, 'error');
    }
}

async function loadAllDocuments() {
    try {
        const response = await fetch(`${API_BASE}/documents`);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const documents = await response.json();

        const container = document.getElementById('allDocuments');
        container.innerHTML = '';

        if (!Array.isArray(documents)) {
            throw new Error('Ungültige Antwort vom Server');
        }

        if (documents.length === 0) {
            container.innerHTML = '<p>Keine Dokumente gefunden</p>';
            return;
        }

        documents.forEach(doc => {
            const div = document.createElement('div');
            div.className = 'document';
            div.innerHTML = `
                <div class="document-title">${doc.title}</div>
                <div>${doc.content}</div>
                <div class="document-actions">
                    <button onclick="deleteDocument('${doc.id}')">Löschen</button>
                </div>
            `;
            container.appendChild(div);
        });
    } catch (error) {
        showMessage('Fehler beim Laden der Dokumente: ' + error.message, 'error');
    }
}

async function deleteDocument(docId) {
    if (!confirm('Sind Sie sicher, dass Sie dieses Dokument löschen möchten?')) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/documents/${docId}`, {
            method: 'DELETE'
        });

        const result = await response.json();

        if (result.status === 'deleted') {
            showMessage('Dokument erfolgreich gelöscht');
            loadAllDocuments();
        } else {
            showMessage('Fehler beim Löschen des Dokuments', 'error');
        }
    } catch (error) {
        showMessage('Fehler: ' + error.message, 'error');
    }
}

// Load all documents on page load
document.addEventListener('DOMContentLoaded', loadAllDocuments);