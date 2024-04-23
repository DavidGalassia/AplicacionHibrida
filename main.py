import tkinter as interfaz #importamos la libreria para crear la interfaz 
from tkinter import messagebox
# Clase Usuario que va a interactuar con el sistema
class Usuario:
    def __init__(self, nombre_usuario, contraseña, peso=0, altura=0): #metodo constructor de la clase usuario
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.peso = peso
        self.altura = altura
        self.meta = ""
# Clase PaginaBienvenida
class PaginaBienvenida:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Bienvenido")
        self.ventana_principal.geometry("3000x3000")#creamos la ventana y definimos los pixeles
        etiqueta = interfaz.Label(ventana_principal, text="¡Bienvenido a MINDFUL GAINS! \U0001F600 ", font=("Comic Sans MS", 28))
        etiqueta.pack(pady=300)#ponemos el widget y lo bajamos 300 pixeles
        #creamos el boton para interactuar
        boton_aceptar = interfaz.Button(ventana_principal, text="Aceptar Términos y Condiciones", font=("Helvetica", 16), command=self.abrir_pagina_inicio)
        boton_aceptar.pack()
        ventana_principal.configure(bg="#F39C12")#fondo de pantalla 
#metodo
    def abrir_pagina_inicio(self):
        self.ventana_principal.destroy()
        pagina_inicio = PaginaInicio()

# Clase PaginaInicio
class PaginaInicio:
    def __init__(self):#metodo constructor
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Inicio de sesión")
        self.ventana_principal.geometry("3000x3000")
        self.nombre_usuario=interfaz.StringVar()#definimos las variables para guardar los datos de usuario y contraseña y validarlos
        self.contraseña=interfaz.StringVar()
        #creacion de los botones
        etiqueta_nombre=interfaz.Label(self.ventana_principal,text="Nombre de Usuario:",font=("Helvetica",18))
        etiqueta_nombre.pack()
        entrada_nombre=interfaz.Entry(self.ventana_principal, textvariable=self.nombre_usuario,font=("Helvetica",16))
        entrada_nombre.pack()
        etiqueta_contraseña = interfaz.Label(self.ventana_principal, text="Contraseña:",font=("Helvetica",18))
        etiqueta_contraseña.pack()
        entrada_contraseña = interfaz.Entry(self.ventana_principal, textvariable=self.contraseña,show="*",font=("Helvetica", 16))
        entrada_contraseña.pack()
        boton_inicio=interfaz.Button(self.ventana_principal, text="Iniciar sesión",font=("Helvetica", 16), command=self.iniciar_sesion)
        boton_inicio.pack()
        boton_registro=interfaz.Button(self.ventana_principal, text="Registrarse",font=("Helvetica", 16), command=self.abrir_pagina_registro)
        boton_registro.pack()

    def iniciar_sesion(self):
        nombre_usuario=self.nombre_usuario.get()
        contraseña=self.contraseña.get()
        if nombre_usuario in claves_usuarios:
        #validamos que el usuario si este en nuestro diccionario (base de datos)
            if claves_usuarios[nombre_usuario].contraseña==contraseña:
                messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
                self.ventana_principal.destroy()
                pagina_meta=PaginaMeta(claves_usuarios[nombre_usuario])
            else:
                messagebox.showerror("Inicio de sesión", "Contraseña incorrecta.")
        else:
            messagebox.showerror("Inicio de sesión", "Usuario no encontrado.")
    def abrir_pagina_registro(self):
        self.ventana_principal.destroy()#cerramos la ventana
        pagina_registro = PaginaRegistro()#llamamos la clase de pagina de registro

# Clase PaginaRegistro
class PaginaRegistro:
    def __init__(self):#constructor definiendo datos que vamos a utilizar
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Registro")
        self.ventana_principal.geometry("3000x3000")
        self.nombre_usuario = interfaz.StringVar()
        self.contraseña = interfaz.StringVar()
        self.peso = interfaz.DoubleVar()
        self.altura = interfaz.DoubleVar()
        #creamos los botones para el registro del peso,altura, usuario y clave(pedidas al usuario)
        etiqueta_nombre = interfaz.Label(self.ventana_principal, text="Nombre de Usuario:", font=("Helvetica", 18))
        etiqueta_nombre.pack()
        entrada_nombre = interfaz.Entry(self.ventana_principal, textvariable=self.nombre_usuario, font=("Helvetica", 16))
        entrada_nombre.pack()
        etiqueta_contraseña = interfaz.Label(self.ventana_principal, text="Contraseña:", font=("Helvetica", 18))
        etiqueta_contraseña.pack()
        entrada_contraseña = interfaz.Entry(self.ventana_principal, textvariable=self.contraseña, show="*", font=("Helvetica", 16))
        entrada_contraseña.pack()
        etiqueta_peso = interfaz.Label(self.ventana_principal, text="Peso (kg):", font=("Helvetica", 18))
        etiqueta_peso.pack()
        entrada_peso = interfaz.Entry(self.ventana_principal, textvariable=self.peso, font=("Helvetica", 16))
        entrada_peso.pack()
        etiqueta_altura = interfaz.Label(self.ventana_principal, text="Altura (m):", font=("Helvetica", 18))
        etiqueta_altura.pack()
        entrada_altura = interfaz.Entry(self.ventana_principal, textvariable=self.altura, font=("Helvetica", 16))
        entrada_altura.pack()
        boton_registro = interfaz.Button(self.ventana_principal, text="Registrarse", font=("Helvetica", 16), command=self.registrarse)
        boton_registro.pack()
#validamos el registro con un mensaje de confirmacion
    def registrarse(self):
        nombre_usuario = self.nombre_usuario.get()
        contraseña = self.contraseña.get()
        peso = self.peso.get()
        altura = self.altura.get()
        nuevo_usuario = Usuario(nombre_usuario, contraseña, peso, altura)
        claves_usuarios[nombre_usuario] = nuevo_usuario
        messagebox.showinfo("Registro", "¡Registro exitoso!")
        self.ventana_principal.destroy()
        pagina_meta = PaginaMeta(nuevo_usuario)

# Clase PaginaMeta
class PaginaMeta:
    def __init__(self, usuario):
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Cuál es tu meta")
        self.ventana_principal.geometry("3000x3000")
        self.usuario = usuario
        etiqueta = interfaz.Label(self.ventana_principal, text="Selecciona tu meta de fitness:", font=("Helvetica", 18))
        etiqueta.pack(pady=250)
        #mostramos las opciones con un ciclo for y su respectivo boton
        metas = ["Bajar de peso", "Subir de peso", "Aumentar masa muscular", "Aumentar fuerza"]
        for meta in metas:
            boton = interfaz.Button(self.ventana_principal, text=meta, font=("Helvetica", 16), command=lambda m=meta: self.abrir_pagina_siguiente(m))
            boton.pack()
#el usuario escoge si quiere ver la dieta o la rutina del plan que habia escogido
    def abrir_pagina_siguiente(self, meta):
        self.usuario.meta = meta
        self.ventana_principal.destroy()
        pagina_dieta_o_rutina = DietaOrutina(self.usuario)

# Clase DietaOrutina
class DietaOrutina:
    def __init__(self, usuario):#constructor
        self.ventana_principal=interfaz.Tk()
        self.ventana_principal.title("Dieta o rutina")
        self.ventana_principal.geometry("3000x3000")
        self.usuario=usuario
        etiqueta = interfaz.Label(self.ventana_principal, text="¿Que quieres ver?", font=("Helvetica", 18))
        etiqueta.pack(pady=250)
        boton_dieta= interfaz.Button(self.ventana_principal, text="Dieta", font=("Helvetica", 16), command=self.abrir_pagina_dieta)
        boton_dieta.pack()
        boton_rutina =interfaz.Button(self.ventana_principal, text="Rutina", font=("Helvetica", 16), command=self.abrir_pagina_rutina)
        boton_rutina.pack()
    def abrir_pagina_dieta(self):
        self.ventana_principal.destroy()
        pagina_dieta = PaginaDieta(self.usuario)
    def abrir_pagina_rutina(self):
        self.ventana_principal.destroy()
        pagina_rutina = PaginaRutina(self.usuario)
# Clase PaginaDieta
class PaginaDieta:
#creamos el mensaje base
    def __init__(self, usuario):
        self.ventana_principal=interfaz.Tk()
        self.ventana_principal.title("Dieta Personalizada")
        self.ventana_principal.geometry("3000x3000")
        self.usuario=usuario
        etiqueta=interfaz.Label(self.ventana_principal, text=f"Dieta personalizada para {self.usuario.nombre_usuario} para el objetivo de {self.usuario.meta}", font=("Helvetica", 18))
        etiqueta.pack(pady=250)
        mensaje = self.obtener_mensaje_dieta()
        etiqueta_mensaje = interfaz.Label(self.ventana_principal, text=mensaje, font=("Helvetica", 14))
        etiqueta_mensaje.pack(pady=10)
#se obtiene el mensaje personalizado
    def obtener_mensaje_dieta(self):
        if self.usuario.meta=="Bajar de peso":
            return "Prioriza alimentos integrales, vegetales, proteínas magras y controla las porciones. Evita alimentos procesados y azúcares refinados. Bebe agua y haz ejercicio regularmente."
        elif self.usuario.meta=="Subir de peso":
            return "Incrementa el consumo de calorías saludables como nueces, aguacate, y carbohidratos complejos. Incluye proteínas magras y realiza ejercicios de fuerza para ganar masa muscular."
        elif self.usuario.meta=="Aumentar masa muscular":
            return "Consume suficientes proteínas de calidad, carbohidratos complejos y grasas saludables. Realiza entrenamiento de fuerza con progresión gradual y descanso adecuado para permitir la recuperación muscular."
        elif self.usuario.meta== "Aumentar fuerza":
            return "Prioriza proteínas para la reparación muscular, carbohidratos para la energía y grasas saludables para el funcionamiento óptimo del cuerpo. Realiza ejercicios compuestos como sentadillas, peso muerto y press de banca, incrementando gradualmente la carga."
        else:
            return "Meta no reconocida."

# Clase PaginaRutina
class PaginaRutina:
#creamos el mensaje base con los datos base
    def __init__(self, usuario):
        self.ventana_principal = interfaz.Tk()
        self.ventana_principal.title("Rutina Personalizada")
        self.ventana_principal.geometry("3000x3000")
        self.usuario = usuario
        etiqueta = interfaz.Label(self.ventana_principal, text=f"Rutina personalizada para {self.usuario.nombre_usuario} para el objetivo de {self.usuario.meta}", font=("Arial", 30))
        etiqueta.pack(pady=250)
        mensaje = self.obtener_mensaje_rutina()
        etiqueta_mensaje=interfaz.Label(self.ventana_principal, text=mensaje, font=("Helvetica", 14))
        etiqueta_mensaje.pack(pady=10)
#damos la rutina personalizada
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
#invocamos el main para que el archivo se ejcutew
def main():
    ventana_principal=interfaz.Tk()
    pagina_bienvenida=PaginaBienvenida(ventana_principal)
    ventana_principal.mainloop()#mantiene la interfaz grafica abierta
if __name__ == "__main__":
    claves_usuarios = { #diccionario con usuarios "existentes" para validar en las pruebas de inicio de sesion
        "valentina": Usuario("valentina", "123", 48, 1.56),
        "juan": Usuario("juan", "juan123", 71, 1.77)
    }
    main()
