import tkinter as interfaz#importamos la libreria que nos permite tener la interfaz grafica
from tkinter import messagebox
#primera clase del usuario que es el que va a interactuar con el sistema
class Usuario:
    def __init__(self,nombre_usuario,contraseña,peso=0,altura=0):#contrusctor
        self.nombre_usuario=nombre_usuario
        self.contraseña=contraseña
        self.peso=peso
        self.altura=altura
        self.meta=""
        #definimos los atributos del usuario de la app
#clase para la pagina de bienvenida        
class PaginaBienvenida:
    def __init__(self,ventana_principal): #constructor
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Bienvenido")
        self.ventana_principal.geometry("3000x3000")#dimensiones de la pantalla 
        etiqueta =interfaz.Label(ventana_principal, text="¡Bienvenido a MINDFUL GAINS! \U0001F600 ", font=("Comic Sans MS", 28))
        etiqueta.pack(pady=300)#ponemos el widget dentro de la ventana con un espacio de 300 px
        #creamos el boton para seguir a la otra pagina
        boton_aceptar = interfaz.Button(ventana_principal, text="Aceptar Términos y Condiciones", font=("Helvetica", 16), command=self.abrir_pagina_inicio)
        boton_aceptar.pack() # Empaqueta el botón en la ventana
        ventana_principal.configure(bg="#F39C12")#ponemos fondo de color naranja
    def abrir_pagina_inicio(self):
        self.ventana_principal.destroy()#cerramos la ventana principal
        pagina_inicio = PaginaInicio()
        messagebox.showinfo("Confirmacion","términos y condiciones aceptados ")
#clase para la pagina de inicio de la app
class PaginaInicio:
    def __init__(self):
    #definimos el titulo y las variables a almacenar
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Inicio de sesion")
        self.ventana_principal.geometry("3000x3000")
        self.nombre_usuario= interfaz.StringVar()
        self.contraseña=interfaz.StringVar()
        #creamos las etiquetas para que inicie sesion o se registre el usuario
        etiqueta_nombre=interfaz.Label(self.ventana_principal, text="Nombre de Usuario:", font=("Helvetica", 18))
        etiqueta_nombre.pack()
        entrada_nombre =interfaz.Entry(self.ventana_principal, textvariable=self.nombre_usuario, font=("Helvetica", 16))
        entrada_nombre.pack()
        etiqueta_contraseña = interfaz.Label(self.ventana_principal, text="Contraseña:", font=("Helvetica", 18))
        etiqueta_contraseña.pack()
        entrada_contraseña = interfaz.Entry(self.ventana_principal, textvariable=self.contraseña, show="*", font=("Helvetica", 16))
        entrada_contraseña.pack()
        boton_inicio=interfaz.Button(self.ventana_principal, text="Iniciar sesion", font=("Helvetica", 16), command=self.iniciar_sesion)
        boton_inicio.pack()
        boton_registro= interfaz.Button(self.ventana_principal, text="Registrarse", font=("Helvetica", 16), command=self.abrir_pagina_registro)
        boton_registro.pack()
#metodo para iniciar sesion
    def iniciar_sesion(self):
        nombre_usuario = self.nombre_usuario.get()
        contraseña = self.contraseña.get()
        if nombre_usuario in claves_usuarios:
            if claves_usuarios[nombre_usuario].contraseña == contraseña:
                messagebox.showinfo("Inicio de sesion", "¡Inicio de sesión exitoso!")
                self.ventana_principal.destroy()
                pagina_meta = PaginaMeta(claves_usuarios[nombre_usuario])
            else:
                messagebox.showerror("Inicio de sesion", "Contraseña incorrecta.")
        else:
            messagebox.showerror("inicio de sesion", "Usuario no encontrado.")
#otro metodo
    def abrir_pagina_registro(self):
        self.ventana_principal.destroy()
        pagina_registro = PaginaRegistro()
#clase para la pagina de registro del usuario
class PaginaRegistro:
    def __init__(self): #coonstructor
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Registro")
        self.ventana_principal.geometry("3000x3000")
        self.nombre_usuario=interfaz.StringVar()
        self.contraseña=interfaz.StringVar()
        self.peso=interfaz.DoubleVar()
        self.altura= interfaz.DoubleVar()
        etiqueta_nombre=interfaz.Label(self.ventana_principal, text="Nombre de Usuario:", font=("Helvetica", 18))
        etiqueta_nombre.pack()
        entrada_nombre= interfaz.Entry(self.ventana_principal, textvariable=self.nombre_usuario, font=("Helvetica", 16))
        entrada_nombre.pack()
        etiqueta_contraseña= interfaz.Label(self.ventana_principal, text="Contraseña:", font=("Helvetica", 18))
        etiqueta_contraseña.pack()
        entrada_contraseña= interfaz.Entry(self.ventana_principal, textvariable=self.contraseña, show="*", font=("Helvetica", 16))
        entrada_contraseña.pack()
        etiqueta_peso= interfaz.Label(self.ventana_principal, text="Peso (kg):", font=("Helvetica", 18))
        etiqueta_peso.pack()
        entrada_peso= interfaz.Entry(self.ventana_principal, textvariable=self.peso, font=("Helvetica", 16))
        entrada_peso.pack()
        etiqueta_altura=interfaz.Label(self.ventana_principal, text="Altura (m):", font=("Helvetica", 18))
        etiqueta_altura.pack()
        entrada_altur =interfaz.Entry(self.ventana_principal, textvariable=self.altura, font=("Helvetica", 16))
        entrada_altura.pack()
        boton_registro=interfaz.Button(self.ventana_principal, text="Registrarse", font=("Helvetica", 16), command=self.registrarse)
        boton_registro.pack()
#metodo para registrarse
    def registrarse(self):
        nombre_usuario=self.nombre_usuario.get()
        contraseña=self.contraseña.get()
        peso= self.peso.get()
        altura= self.altura.get()
        nuevo_usuario= Usuario(nombre_usuario, contraseña, peso, altura)
        claves_usuarios[nombre_usuario]= nuevo_usuario
        messagebox.showinfo("Registro", "¡Registro exitoso!")
        self.ventana_principal.destroy()
        #llamamos la clase
        pagina_meta = PaginaMeta(nuevo_usuario)
#clase para seleccionar la meta
class PaginaMeta:
    def __init__(self, usuario):
        self.ventana_principal=interfaz.Tk()
        self.ventana_principal.title("Cuál es tu meta")
        self.ventana_principal.geometry("3000x3000")
        self.usuario=usuario
        etiqueta=interfaz.Label(self.ventana_principal, text="Selecciona tu meta de fitness:", font=("Helvetica", 18))
        etiqueta.pack(pady=250)
        metas = ["Bajar de peso", "Subir de peso", "Aumentar masa muscular", "Aumentar fuerza"]
        # Creamos botones para cada meta
        for meta in metas:
        # Creamos una función anónima que pasa el valor de la meta como argumento a abrir_pagina_siguiente
            def crear_funcion(meta=meta):
                self.abrir_pagina_siguiente(meta)
        # Creamos el botón con la meta como texto y la función anónima como comando
        boton = interfaz.Button(self.ventana_principal, text=meta, font=("Helvetica", 16), command=crear_funcion)
        boton.pack()
#metodo para seguir segun lo seleccionado
    def abrir_pagina_siguiente(self, meta):
        self.usuario.meta = meta
        self.ventana_principal.destroy()
        pagina_dieta_o_rutina = DietaOrutina(self.usuario)
#clase para preguntar si el usuario quiere ver la dieta o la rutina
class DietaOrutina:
    def __init__(self, usuario):
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Dieta o Rutina")
        self.ventana_principal.geometry("3000x3000")
        self.usuario = usuario
        etiqueta = interfaz.Label(self.ventana_principal, text="¿Qué prefieres ver?", font=("Helvetica", 18))
        etiqueta.pack(pady=250)
        boton_dieta = interfaz.Button(self.ventana_principal, text="Dieta", font=("Helvetica", 16), command=self.abrir_pagina_dieta)
        boton_dieta.pack()
        boton_rutina = interfaz.Button(self.ventana_principal, text="Rutina", font=("Helvetica", 16), command=self.abrir_pagina_rutina)
        boton_rutina.pack()
#metodos 
    def abrir_pagina_dieta(self):
        self.ventana_principal.destroy()
        pagina_dieta = PaginaDieta(self.usuario)
    def abrir_pagina_rutina(self):
        self.ventana_principal.destroy()
        pagina_rutina = PaginaRutina(self.usuario)
#clase de la pagina que muestra la dieta recomendada
class PaginaDieta:
    def __init__(self, usuario):
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Dieta Personalizada")
        self.ventana_principal.geometry("3000x3000")
        self.usuario =usuario
        etiqueta =interfaz.Label(self.ventana_principal,text=f"Dieta personalizada para {self.usuario.nombre_usuario} para el objetivo de {self.usuario.meta}", font=("Helvetica", 18))
        etiqueta.pack(pady=250)
        mensaje=self.obtener_mensaje_dieta()
        etiqueta_mensaje=interfaz.Label(self.ventana_principal,text=mensaje,font=("Helvetica",14))
        etiqueta_mensaje.pack(pady=10)
#metodo para que salga el mensaje de la dieta
    def obtener_mensaje_dieta(self):
        if self.usuario.meta=="Bajar de peso":
            return "Prioriza alimentos integrales, vegetales, proteínas magras y controla las porciones. Evita alimentos procesados y azúcares refinados. Bebe agua y haz ejercicio regularmente."
        elif self.usuario.meta=="Subir de peso":
            return "Incrementa el consumo de calorías saludables como nueces, aguacate, y carbohidratos complejos. Incluye proteínas magras y realiza ejercicios de fuerza para ganar masa muscular."
        elif self.usuario.meta=="Aumentar masa muscular":
            return "Consume suficientes proteínas de calidad, carbohidratos complejos y grasas saludables. Realiza entrenamiento de fuerza con progresión gradual y descanso adecuado para permitir la recuperación muscular."
        elif self.usuario.meta=="Aumentar fuerza":
            return "Prioriza proteínas para la reparación muscular, carbohidratos para la energía y grasas saludables para el funcionamiento óptimo del cuerpo. Realiza ejercicios compuestos como sentadillas, peso muerto y press de banca, incrementando gradualmente la carga."
        else:
            return "Meta no reconocida."
#clase de la pagina que muestra la rutina
class PaginaRutina:
    def __init__(self,usuario):
        self.ventana_principal=interfaz.Tk()
        self.ventana_principal.title("Rutina Personalizada")
        self.ventana_principal.geometry("3000x3000")
        self.usuario = usuario
        etiqueta=interfaz.Label(self.ventana_principal, text=f"Rutina personalizada para {self.usuario.nombre_usuario} para el objetivo de {self.usuario.meta}", font=("Arial", 30))
        etiqueta.pack(pady=250)
        mensaje=self.obtener_mensaje_rutina()
        etiqueta_mensaje=interfaz.Label(self.ventana_principal,text=mensaje,font=("Helvetica", 14))
        etiqueta_mensaje.pack(pady=10)
#metodo para que salga el mensaje de la rutina
    def obtener_mensaje_rutina(self):
        if self.usuario.meta=="Bajar de peso":
            return "Cardio (caminata rápida/correr) - 4 sets de 20 minutos. Entrenamiento de fuerza (peso corporal/pesas ligeras) - 3 sets de 12-15 repeticiones."
        elif self.usuario.meta=="Subir de peso":
            return "Entrenamiento de fuerza (pesas) - 4-5 sets de 6-8 repeticiones. Ejercicios compuestos (sentadillas, press de banca, peso muerto)."
        elif self.usuario.meta=="Aumentar masa muscular":
            return "Entrenamiento de fuerza (pesas) - 4 sets de 8-12 repeticiones. Enfoque en ejercicios multiarticulares (sentadillas, dominadas, press de banca)."
        elif self.usuario.meta=="Aumentar fuerza":
            return "Entrenamiento de fuerza (pesas) - 4 sets de 8-12 repeticiones. Enfoque en ejercicios multiarticulares (sentadillas, dominadas, press de banca)."
        else:
            return "Meta no reconocida."
 #ejecutamos el archuvo           
def main():
    ventana_principal = interfaz.Tk() 
    pagina_bienvenida = PaginaBienvenida(ventana_principal)
    ventana_principal.mainloop()
if __name__=="__main__":
    claves_usuarios={
        "usuario1":Usuario("valentina","123",48,1.56),
        "usuario2":Usuario("juan","juan123",71,1.77)
    }
    main()
