#!/usr/bin/python3
def generate_invitations(template_content, attendees):
    """
    Génère des fichiers d'invitations à partir d'un template et d'une liste de participants.

    Args:
        template (str): Le contenu du template avec des placeholders {name}, {event_title}, {event_date}, {event_location}.
        attendees (list of dict): Liste de dictionnaires contenant les informations des participants.
    """
    if not isinstance(template_content, str):
        print(f"Error: template_content is not a string {type(template_content).__name__}")
        return

    if not isinstance(attendees, list) or not\
            all(isinstance(x, dict) for x in attendees):
        print(f"Error: attendees is not a list of dictionaries {type(attendees).__name__}")
        return

    if template_content == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    length = 0
    for person in attendees:
        with open(f"output_{length}.txt", "a") as file:
            file.write(template_content.format(
                name=person.get('name') or "N/A",
                event_title=person.get('event_title') or "N/A",
                event_date=person.get('event_date') or "N/A",
                event_location=person.get('event_location') or "N/A"
            ))
        length += 1
