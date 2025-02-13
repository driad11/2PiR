import streamlit as st
import requests
import Image

img_contact_form = Image.open("images/logo")


st.title("Willkommen!")

with st.container():
    st.write("---")
    st.header("Angebot")
    st.write("##")
    image_column, text_column = ((1,2))
    with image_column:
        st.image(img_contact_form)

    with text_column:
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


