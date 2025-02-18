import streamlit as st

logo_url = "https://raw.githubusercontent.com/driad11/websitetest/main/statics/logo.jpg"

st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            position: relative;
        }}

        .logo-container {{
            position: absolute !important;
            top: 10px !important;  /* Adjust as needed */
            right: 10px !important; /* Adjust as needed */
            width: 120px !important;
            height: auto !important;
            z-index: 1000 !important;
            margin-top: -20px;  /* Move up */
            margin-right: 90px; /* Move left */
        }}
    </style>
    <div class="logo-container">
        <img src="{logo_url}" width="120">
    </div>
    """,
    unsafe_allow_html=True
)


st.title("Willkommen!")


st.write("""
    Egal, ob eine einfache Renovierung, ein Umbau, ein Anbau oder eine Sanierung: 
    Wir begleiten den Prozess vom Anfang der Planung bis zum Abschluss der Maßnahmen 
    Wir unterstützen hinsichtlich der Entscheidung, welche Maßnahmen baulich sinnvoll, geboten und im Rahmen eines Budgets wirtschaftlich machbar sind. 
    Wir helfen auch bei der Bestimmung des notwendigen Budgets durch eine detaillierte Kostenschätzung
    Wir erstellen oder unterstützen bei der Erstellung eines Bauablaufplans und sorgen für die Überwachung und Erreichung der gesetzten Ziele.
    Wir unterstützen, soweit durch Baumaßnahmen rechtliche Belange betroffen sind (z. B. notwendige Baugenehmigung) und können bei Bedarf auch Fördermöglichkeiten prüfen
      Soweit dritte Unternehmen für Bauleistungen beauftragt werden sollen/müssen, übernehmen wir folgende Leistungen:  
      die Einholung von Angeboten und die Beauftragung in Ihrem Namen, 
      die Abrechnung und Kostenkontrolle,
      die Bauüberwachung der Leistungen nach vorheriger Zieldefinition
     wir erstellen ein Bautagebuch als Dokumentation des Baufortschritts und zur Überwachung der Kosten
     bei Bedarf können wir einzelne Baumaßnahmen persönlich übernehmen """)







