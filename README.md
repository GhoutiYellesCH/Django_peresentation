# 🐍 Django Rapid Development Demo (University Project)

## 🎯 Aperçu du Projet
Ce projet est une application web construite avec Django (Python) pour servir de support à une présentation universitaire. Il démontre la rapidité de développement, la structure claire et les mécanismes de sécurité intégrés du framework.

### Fonctionnalités Démontrées (Phases)
| Phase | Concept | Route de Démo |
| :--- | :--- | :--- |
| **1 & 2** | Architecture **MVT** & **ORM** (Base de données) | `/mvt/` & `/articles/` |
| **3** | Système de **Templates** (Héritage) | `/templates/` |
| **4** | **Sécurité** & **Authentification** (CSRF, XSS) | `/security/` |
| **5** | **Dashboard** Dynamique (Données ORM) | `/dashboard/` |
| **6** | **API Endpoints** (Exposer les données en JSON) | `/api/intro/` |

---

## 🛠️ Installation et Exécution

### Prérequis
* Python 3.8+
* `pip` et `venv`

### 1. Cloner le Répertoire
```bash
# Assurez-vous d'avoir cloné votre projet ou d'être dans le dossier racine
cd D:\code\python\django_presentation
````

### 2\. Créer et Activer l'Environnement Virtuel

```bash
python -m venv venv
# Sur Windows:
.\venv\Scripts\activate 
# Sur Linux/macOS:
source venv/bin/activate
```

### 3\. Installer les Dépendances

```bash
pip install -r requirements.txt
```

### 4\. Appliquer les Migrations

Ceci crée la base de données SQLite et la table `Article`.

```bash
python manage.py migrate
```

### 5\. Créer un Superutilisateur (pour l'Admin et le Dashboard)

Entrez un nom d'utilisateur et un mot de passe pour tester l'authentification.

```bash
python manage.py createsuperuser
```

### 6\. Lancer le Serveur de Développement

```bash
python manage.py runserver
```

### 7\. Tester

  * Ouvrez votre navigateur à **`http://127.0.0.1:8000/`**
  * **Ajouter des données:** Rendez-vous sur **`http://127.0.0.1:8000/admin/`** et connectez-vous avec le superutilisateur pour ajouter quelques articles.
  * **Tester le Dashboard:** Connectez-vous via le lien **Connexion** de la barre de navigation, puis accédez à la page **Dashboard**.

-----

## 📄 Fichiers Clés

| Fichier | Rôle | Phases |
| :--- | :--- | :--- |
| `presentation/models.py` | Définit le modèle `Article` (ORM). | 2, 5, 6 |
| `presentation/views.py` | Contient la logique Python (MVT, ORM, API). | 1, 2, 5, 6 |
| `presentation/urls.py` | Gère le routage des URL. | 1-6 |
| `presentation/templates/base.html` | Layout global, navigation, et design. | 3, 7 |
| `django_presentation/settings.py` | Configuration de sécurité et d'authentification. | 4 |
