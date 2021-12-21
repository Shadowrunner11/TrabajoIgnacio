from modelo import actualizarCama, actualizarPaciente, actualizarServicio, camasVacias, eliminarPaciente, ingresarPaciente, insertarPaciente, readCamas, readPacientes, readServicio

seleccion2=0
class Menu:
    def __init__(self,*arg):
       self.opciones=arg
    def __str__(self) -> str:
        texto="seleccione una opcion"
        for i in range(len(self.opciones)):
            texto+=f"\n{i+1} - {self.opciones[i]}"
        return texto+"\n"

  
def wrapCrearPaciente ():
    insertarPaciente(input("Inserte el nombre\n"), input("Inserte RUT del paciente\n"),input("Ingrese la fecha de nacimiento\n"))
    print("Paciente creado con èxito")

def wrapEliminarPaciente ():
    eliminarPaciente(input("Nombre del paciente\n"))
    print("Paciente eliminado con èxito")

def wrapEditarPaciente ():
    actualizarPaciente(input("Ingrese el nombre del paciente\n"), input("Ingrese nombre nuevo"))

def wrapActualizarCama ():
    actualizarCama(input("Ingrese le nombre de la cama\n"), input("Ingrese el nuevo nombre de la cama\n"))
def wrapActualizarServicio ():
    actualizarServicio(input("Ingrese el nombre del servicio\n", input("Ingrese el nuevo nombre del servicio\n")))

def wrapIngresarPaciente ():
    ingresarPaciente(input("Nombre del paciente\n"), input("Nombre de la cama\n"), input ("Fecha de inicio"), input("Fecha final"))


def menuInput (menu):
    seleccion2 = input(menu)
    menuprincipal[int(seleccion)-1][int(seleccion2)]()
  
menuprincipal=[
    [lambda : menuInput(Menu("Crear", "Editar","Listar","Eliminar")),
    wrapCrearPaciente,
    wrapEditarPaciente,
    readPacientes,
    wrapEliminarPaciente
    ],
    [lambda : menuInput(Menu("Consultar cama", "Editar cama", "Consultar servicios", "Editar servicios")),
    readCamas,
    wrapActualizarCama,
    readServicio,
    wrapActualizarServicio,

    ],
    [lambda : menuInput(Menu("Ingresar paciente", "Consultar camas disponibles")),
    wrapIngresarPaciente,
    camasVacias,
    ]
]
seleccion=input(Menu("Pacientes","Mantenedores","Gestiòn de camas"))

menuprincipal[int(seleccion)-1][int(seleccion2)]()