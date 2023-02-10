from jinja2 import Environment, FileSystemLoader
from html2image import Html2Image

def generate_file(output_path, title, author, type, date, salle):
    environment = Environment(loader=FileSystemLoader("template/"))
    template = environment.get_template("template.html")

    rend = template.render(title=title, author=author, type=type, date=date, salle=salle)

    hti = Html2Image()
    hti.load_file('template/illustration_1.png')
    hti.load_file('template/logo_pyconfr_1.png')
    hti.screenshot(
        html_str=rend, css_file='template/styles.css',
        save_as=output_path,
        size=(1200,675)
    )

if __name__ =="__main__":
    generate_file(output_path="rend.png",
                  title= "Accessibilité numérique : faire sa part quand on est développeur·euse backend",
                  author= "Amaury Carrade",
                  type= "Conférence",
                  date= "Samedi 18 février 11H00",
                  salle= "Salle Rosalind Franklin")