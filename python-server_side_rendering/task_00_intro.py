#!/usr/bin/python3
import os

def generate_invitations(template_content, attendees):
    """
    Génère des fichiers d'invitations à partir d'un template et d'une liste de participants.
    """
    if not isinstance(template_content, str):
        print(f"Error: template_content is not a string ({type(template_content).__name__})")
        return

    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print(f"Error: attendees is not a list of dictionaries ({type(attendees).__name__})")
        return

    if template_content == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    index = 1
    for person in attendees:
        invitation = template_content

        invitation = invitation.replace("{name}", str(person.get("name") or "N/A"))
        invitation = invitation.replace("{event_title}", str(person.get("event_title") or "N/A"))
        invitation = invitation.replace("{event_date}", str(person.get("event_date") or "N/A"))
        invitation = invitation.replace("{event_location}", str(person.get("event_location") or "N/A"))

        filename = f"output_{index}.txt"

        try:
            if os.path.exists(filename):
                print(f"Warning: {filename} already exists, it will be overwritten.")
        
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")

        index += 1
