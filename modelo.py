import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import pymysql

motor=sa.create_engine("mysql+pymysql://root:@localhost/clinica")
Base=declarative_base()
metadatos=sa.MetaData(motor)
metadatos.reflect()

class Camas(Base):
    __table__=sa.Table("camas",metadatos)

class Cama_Paciente(Base):
    __table__=sa.Table("cama_paciente",metadatos)

class Hitorial_medico_cama(Base):
    __table__=sa.Table("hitorial_medico_cama",metadatos)

class Medicos(Base):
    __table__=sa.Table("medicos",metadatos)

class Pacientes(Base):
    __table__=sa.Table("pacientes",metadatos)

class Servicios_clinicos(Base):
    __table__=sa.Table("servicios_clinicos",metadatos)

sesion=sa.orm.sessionmaker(motor)
sesionfinal=sesion()

def insertarPaciente (nombrePaciente, rutPaciente, fecha):
    sesionfinal.add(Pacientes(NombrePaciente=nombrePaciente,
                            RutPaciente=rutPaciente,
                            FechaNacimiento=fecha))
    sesionfinal.commit()

def actualizarPaciente (nombrePaciente, nombreNuevo):
    paciente = sesionfinal.query(Pacientes).filter(Pacientes.NombrePaciente ==nombrePaciente).first()
    paciente.NombrePaciente = nombreNuevo
    sesionfinal.commit()

def readPacientes ():    
    for paciente in sesionfinal.query(Pacientes).all():
        print(paciente.NombrePaciente)

def eliminarPaciente (nombrePaciente):
    sesionfinal.query(Pacientes).filter(Pacientes.NombrePaciente == nombrePaciente).delete()
    sesionfinal.commit()

def readCamas ():
    print("Cama\tId servicio clìnico")
    for cama in sesionfinal.query(Camas).all():
        print(f"{cama.Cama}\t{cama.IdServicioClinico}")

def actualizarCama (nombreCama, nombreNuevo):
    cama = sesionfinal.query(Camas).filter(Camas.Cama==nombreCama).first()
    cama.Cama = nombreNuevo
    sesionfinal.commit()
def readServicio ():
    print ("Nombre del servicio")
    for servicio in sesionfinal.query(Servicios_clinicos).all():
        print(servicio.ServicioClinico)

def actualizarServicio (nombreServicio, nombreNuevo):
    servicio = sesionfinal.query(Servicios_clinicos).filter(Servicios_clinicos.ServicioClinico==nombreServicio).first()
    servicio.ServicioClinico = nombreNuevo
    sesionfinal.commit()

def ingresarPaciente(paciente, cama, inicio, final):
    sesionfinal.add(Cama_Paciente(
        IdCama=sesionfinal.query(Camas).filter(Camas.Cama==cama).first().IdCama,
        IdPaciente=sesionfinal.query(Pacientes).filter(Pacientes.NombrePaciente==paciente).first().IdPaciente,
        FechaInicio=inicio,
        FechaAlta=final
    ))
    sesionfinal.commit()
def camasVacias():
    query=sesionfinal.query(Camas.Cama, sa.func.count(Cama_Paciente.IdCamaPaciente))
    query= query.outerjoin(Cama_Paciente).group_by(Camas.Cama)
    for row in query:
        if (not row[1]):
            print(row[0])
