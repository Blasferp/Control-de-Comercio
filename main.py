import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
import streamlit as st
import pandas as pd
import datetime
import openpyxl
# import streamlit_image_coordinates
from streamlit_option_menu import option_menu
from datetime import datetime
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime

# Agregar CSS personalizado para establecer el fondo abstracto
page_bg_img = '''
<style>
body {
    background-image: url("https://previews.123rf.com/images/altoclassic/altoclassic1602/altoclassic160200001/52670764-fondo-abstracto-l%C3%ADneas-onduladas-de-color-rojo-sobre-un-fondo-punto-gris.jpg");
    background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Obtener el enlace directo a la imagen en Google Drive
image_url = "https://drive.google.com/uc?export=download&id=1d43D8ua672T-FMfdnsMEgK-2PrTvIhKd"

# Descargar la imagen desde el enlace
response = requests.get(image_url)
image_bytes = BytesIO(response.content)

# Cargar la imagen usando PIL (Python Imaging Library)
image = Image.open(image_bytes)

# Ajustar el tamaño de la imagen
width, height = image.size
new_width = int(width * 0.5)  # Reducir el ancho a la mitad
new_height = int(height * 0.5)  # Reducir la altura a la mitad
resized_image = image.resize((new_width, new_height))

# Mostrar la imagen en Streamlit
st.image(resized_image, caption='Imagen desde Google Drive')

# Ahora puedes seguir con el resto de tu código Streamlit aquí
st.title("Mi Aplicación Streamlit")
st.write("Este es el contenido de mi aplicación.")

selected = option_menu(
    menu_title='Menu Principal',
    options=['Home', 'Productos', 'Proveedores', 'Clientes','Ventas', 'Egresos', 'Visualizacion'],
    menu_icon='gear',
    icons=['house', 'bi-basket-fill', 'bi-truck', ' bi-person-fill', 'bi-currency-dollar', 'bi-cash-stack', 'bi-bar-chart'],
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "16px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "lightblue"},
    }
)


####################################################################################################

if selected == 'Home':
    st.title("Bienvenido Alfred! 👋")
    st.write()
    st.markdown(
        """
        Esta aplicación te ayudará a hacer un seguimiento detallado de tu negocio, permitiéndote mantener un control efectivo sobre el mismo.

        
        ### Como Ingresar?!
        **👆 Selecciona en el Menu Principal que se encuentra el la parte superior de la pagina** la opción que desees explorar:
        
        
        ### Que encontraras en cada opcion!
        En cada sección tendrás la capacidad de agregar, modificar y analizar los datos ingresados.

        **Productos:** Aquí encontrarás información relevante sobre tus productos, incluyendo cantidad disponible, precios y más.

        **Proveedores:** Detalles como número de teléfono, dirección y contacto para mantener una comunicación efectiva con tus proveedores.

        **Clientes:** Información detallada sobre tus clientes, incluyendo su información de contacto y ubicación para mejorar las relaciones comerciales.

        **Egresos:** Detalles completos de cada gasto realizado en tu negocio, proporcionando una visión clara de tus costos operativos.

        **Ventas:** Información detallada sobre las ventas realizadas, incluyendo cantidad vendida, cliente asociado y más para un análisis exhaustivo de tus operaciones comerciales.
        
        **Visualización:** Observación de los datos en forma de gráficos para facilitar el análisis y posibilitar la toma de decisiones sobre el negocio.
    """
    )

   
# Obtener la fecha actual en español
meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

dias_semana = [
    "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
]

now = datetime.now()
current_date = f"{dias_semana[now.weekday()]}, {now.day} de {meses[now.month - 1]} de {now.year}"

# En el side bar ingresar una imagen arriba de la fecha
st.sidebar.image("https://github.com/Blasferp/Control-de-Comercio/blob/main/imagen/fondo_pantalla.jpg?raw=true", width=150)

# Agregar líneas en blanco para dejar espacio
st.sidebar.markdown("""\n\n\n""")

# Separar con línea horizontal
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Mostrar la barra lateral con la fecha actual
st.sidebar.title(f'📅Fecha:')
st.sidebar.markdown(
    f'<h1 style="color: #333;">{current_date}</h1>',
    unsafe_allow_html=True
)

# Separar con línea horizontal
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
   
#############################################################################################    
    
if selected == 'Productos':
    st.title(f'🎁 Productos') 
    st.markdown("""
            En esta página se muestra una tabla con los datos de los productos existentes, la cual podrás observar a continuación. 👇

            ***👈 Puedes acceder en la barra lateral*** para agregar nuevos productos o modificar los productos existentes. Selecciona la acción que deseas realizar en el menú desplegable de 'Gestión de productos'.

            Una vez elegida la opción deseada, aparecerán a continuación menús desplegables o campos para rellenar. Puedes agregar o modificar el nombre del producto, la cantidad, el precio de compra y el precio de venta. Una vez que hayas completado los campos, presiona el botón 'Agregar'.

            ¡No te olvides de completar todos los campos! 💪
            """
    )
    # Separador horizontal
    st.markdown("<hr>", unsafe_allow_html=True)  
      
    st.header(f'📅 Tabla de Productos')
    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df():
        try:
            df = pd.read_csv("Productos.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Producto', 'Cantidad', 'Precio_Compra'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df):
        df.to_csv("Productos.csv", index=False)

    # Cargar el DataFrame al inicio de la aplicación
    df = cargar_df()

    # Mostrar el DataFrame actualizado
    st.dataframe(df)

    # Variables para rastrear la acción
    accion_realizada = None
    indice_modificado = None

    # Sidebar
    # Título grande para la selección de gestión de productos
    st.sidebar.title("Gestión de Productos")
    
    # Opciones de la selección de gestión de productos
    accion = st.sidebar.selectbox("Seleccione una acción", ["Agregar Nuevo Producto", "Modificar Producto"])
    
    # Separar con línea horizontal
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    
    if accion == "Agregar Nuevo Producto":
        st.sidebar.title("Agregar Nuevo Producto")
        Nombre_Producto = st.sidebar.text_input('Nombre_Producto:')
        Cantidad = st.sidebar.number_input('Cantidad:', min_value=0, step=1)
        Precio_Compra = st.sidebar.number_input('Precio_Compra:', min_value=0.0)        
        fecha_actual = datetime.now()
        # fecha_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        
        if st.sidebar.button("Agregar"):
            # Cargar el DataFrame existente
            df = cargar_df()

            if not Nombre_Producto:
                st.sidebar.warning("Debe ingresar el nombre del producto.")
            elif Nombre_Producto.lower() in df['Nombre_Producto'].str.lower().values:
                st.sidebar.warning("El producto ya existe. Por favor, elige otro nombre.")
            else:
                # Crear nueva fila con los datos del nuevo producto
                nueva_fila = pd.DataFrame({'Nombre_Producto': [Nombre_Producto],
                                        'Cantidad': [Cantidad],
                                        'Precio_Compra': [Precio_Compra],                                        
                                        'Fecha': [fecha_actual]})
                
                # Concatenar el DataFrame original con el nuevo DataFrame
                df = pd.concat([df, nueva_fila], ignore_index=True)

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Agregado"
                indice_modificado = df.shape[0] - 1  # Í

    elif accion == "Modificar Producto":
        st.sidebar.title("Modificar Producto")
        opciones = df['Nombre_Producto'].tolist()
        producto_modificar = st.sidebar.selectbox("Selecciona un producto:", opciones)

        if producto_modificar:
            indice_modificar = df[df['Nombre_Producto'] == producto_modificar].index[0]
            Nombre_Producto = st.sidebar.text_input('Nombre_Producto:', value=producto_modificar)  # Agregar campo para modificar el nombre
            Cantidad = st.sidebar.number_input('Cantidad:', min_value=0, step=1, value=df.loc[indice_modificar, 'Cantidad'])
            Precio_Compra = st.sidebar.number_input('Precio_Compra:', min_value=0.0, value=df.loc[indice_modificar, 'Precio_Compra'])

            if st.sidebar.button("Modificar"):
                # Actualizar los valores en el DataFrame
                df.loc[indice_modificar, 'Nombre_Producto'] = Nombre_Producto  # Actualizar el nombre del producto
                df.loc[indice_modificar, 'Cantidad'] = Cantidad
                df.loc[indice_modificar, 'Precio_Compra'] = Precio_Compra

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Modificado"
                indice_modificado = indice_modificar
                    
    # Separar el último encabezado del resto del contenido con una línea horizontal
    st.markdown("<hr>", unsafe_allow_html=True)         
        
    # Titulo del Producto modificado            
    st.header("📝 Producto agregado o modificado")

    # Mostrar la fila que se agregó o modificó
    if accion_realizada:
        st.sidebar.success(f"Se ha {accion_realizada} el producto:")
        st.dataframe(df.iloc[indice_modificado:indice_modificado+1])

############################################################################################################

   
if selected == 'Proveedores':    
    st.title(f'🚚 Proveedores') 
    st.markdown("""En esta página se muestra una tabla con los datos de los proveedores existentes, la cual podrás observar a continuación 👇.

***👈 Puedes acceder en la barra lateral*** para agregar nuevos proveedores o modificar los proveedores existentes. Selecciona la acción que deseas realizar en el menú desplegable de 'Gestión de proveedores'.

Una vez elegida la opción deseada, aparecerán a continuación menús desplegables o campos para rellenar. Puedes agregar o modificar el nombre del proveedor, el contacto, el teléfono, el correo electrónico y la dirección. Una vez que hayas completado los campos, presiona el botón 'Agregar' o 'Modificar'.

¡No te olvides de completar todos los campos! 💪""")
    
    # Separar el último encabezado del resto del contenido con una línea horizontal
    st.markdown("<hr>", unsafe_allow_html=True)
                
    st.header(f'📅 Tabla de Proveedores')
    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df():
        try:
            df = pd.read_csv("Proveedores.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Proveedor', 'Contacto', 'Telefono', 'Email', 'Direccion'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df):
        df.to_csv("Proveedores.csv", index=False)

    # Cargar el DataFrame al inicio de la aplicación
    df = cargar_df()

    # Mostrar el DataFrame actualizado
    st.dataframe(df)

    # Variables para rastrear la acción
    accion_realizada = None
    indice_modificado = None

    # Sidebar
    # Título grande para la selección de gestión de proveedores
    st.sidebar.title("Gestión de Proveedores")

    # Opciones de la selección de gestión de proveedores
    accion = st.sidebar.selectbox("Seleccione una acción", ["Agregar Nuevo Proveedor", "Modificar Proveedor"])
    
    # Separar las opciones de gestión de proveedores con una línea horizontal
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    
    
    if accion == "Agregar Nuevo Proveedor":
        st.sidebar.title("Agregar Nuevo Proveedor")
        Nombre_Proveedor = st.sidebar.text_input('Nombre del Proveedor:')
        Contacto = st.sidebar.text_input('Contacto:')
        Telefono = st.sidebar.text_input('Teléfono:')
        Email = st.sidebar.text_input('Email:')
        Direccion = st.sidebar.text_input('Dirección:')
        fecha_actual = datetime.now()
        
        if st.sidebar.button("Agregar"):
            if not all([Nombre_Proveedor, Contacto, Telefono, Email, Direccion]):
                st.sidebar.warning("Todos los campos son obligatorios. Por favor, llene todos los campos.")
            elif Nombre_Proveedor.lower() in df['Nombre_Proveedor'].str.lower().values:
                st.sidebar.warning("El proveedor ya existe. Por favor, elige otro nombre.")
            else:
                # Crear nueva fila con los datos del nuevo proveedor
                nueva_fila = pd.DataFrame({'Nombre_Proveedor': [Nombre_Proveedor],
                                        'Contacto': [Contacto],  # Corregido
                                        'Telefono': [Telefono],
                                        'Email': [Email],
                                        'Direccion': [Direccion],
                                        'Fecha': [fecha_actual]})
                
                # Concatenar el DataFrame original con el nuevo DataFrame
                df = pd.concat([df, nueva_fila], ignore_index=True)

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Agregado"
                indice_modificado = df.shape[0] - 1  # Índice de la fila recién agregada

    elif accion == "Modificar Proveedor":
        st.sidebar.title("Modificar Proveedor")
        opciones = df['Nombre_Proveedor'].tolist()
        Proveedor_modificar = st.sidebar.selectbox("Selecciona un proveedor:", opciones)

        indice_modificar = None  # Para manejar el caso cuando no se selecciona ningún proveedor

        if Proveedor_modificar:
            indice_modificar = df[df['Nombre_Proveedor'] == Proveedor_modificar].index[0]
            Nombre_Proveedor = st.sidebar.text_input('Nombre del Proveedor:', value=df.loc[indice_modificar, 'Nombre_Proveedor'])
            Contacto = st.sidebar.text_input('Contacto:', value=df.loc[indice_modificar, 'Contacto'])  # Corregido
            Telefono = st.sidebar.text_input('Teléfono:', value=df.loc[indice_modificar, 'Telefono'])
            Email = st.sidebar.text_input('Email:', value=df.loc[indice_modificar, 'Email'])
            Direccion = st.sidebar.text_input('Dirección:', value=df.loc[indice_modificar, 'Direccion'])

            if st.sidebar.button("Modificar"):
                if not all([Nombre_Proveedor, Contacto, Telefono, Email, Direccion]):
                    st.sidebar.warning("Todos los campos son obligatorios. Por favor, llene todos los campos.")
                else:
                    # Actualizar los valores en el DataFrame
                    df.loc[indice_modificar, 'Nombre_Proveedor'] = Nombre_Proveedor
                    df.loc[indice_modificar, 'Contacto'] = Contacto  # Corregido
                    df.loc[indice_modificar, 'Telefono'] = Telefono
                    df.loc[indice_modificar, 'Email'] = Email
                    df.loc[indice_modificar, 'Direccion'] = Direccion     

                    # Guardar el DataFrame actualizado
                    guardar_df(df)
                    accion_realizada = "Modificado"
                    indice_modificado = indice_modificar

    # Separar el último encabezado del resto del contenido con una línea horizontal
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.header("📝 Proveedor agregado o modificado")
    # Mostrar la fila que se agregó o modificó
    # Mostrar el proveedor agregado o modificado
    if accion_realizada:
        st.sidebar.success(f"Se ha {accion_realizada} el Cliente:")
        st.dataframe(df.iloc[indice_modificado:indice_modificado+1])

    
############################################################################    
    
    
    
if selected == 'Clientes':    
    st.title(f'👩 Clientes 👨') 
    st.markdown("""En esta página se muestra una tabla con los datos de los clientes existentes, la cual podrás observar a continuación 👇.

***👈 Puedes acceder en la barra lateral*** para agregar nuevos clientes o modificar los clientes existentes. Selecciona la acción que deseas realizar en el menú desplegable de 'Gestión de clientes'.

Una vez elegida la opción deseada, aparecerán a continuación menús desplegables o campos para rellenar. Puedes agregar o modificar el nombre del proveedor, el contacto, el teléfono, el correo electrónico y la dirección. Una vez que hayas completado los campos, presiona el botón 'Agregar' o 'Modificar'.

¡No te olvides de completar todos los campos! 💪""")

    st.header(f'📅 Tabla de Clientes')
    
    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df():
        try:
            df = pd.read_csv("Clientes.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Cliente', 'Contacto', 'Telefono', 'Email', 'Direccion'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df):
        df.to_csv("Clientes.csv", index=False)

    # Cargar el DataFrame al inicio de la aplicación
    df = cargar_df()

    # Mostrar el DataFrame actualizado
    st.dataframe(df)

    # Variables para rastrear la acción
    accion_realizada = None
    indice_modificado = None

    # Sidebar
    # Título grande para la selección de gestión de Clientes
    st.sidebar.title("Gestión de Clientes")
    
    # Opciones de la selección de gestión de Clientes
    accion = st.sidebar.selectbox("Seleccione una acción", ["Agregar Nuevo Cliente", "Modificar Cliente"])
    
    # Separar el último encabezado del resto del contenido con una línea horizontal
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if accion == "Agregar Nuevo Cliente":
        st.sidebar.title("Agregar Nuevo Cliente")
        Nombre_Cliente = st.sidebar.text_input('Nombre_Cliente:')
        Contacto = st.sidebar.text_input('Contacto:')
        Telefono = st.sidebar.text_input('Telefono:')
        Email = st.sidebar.text_input('Email:')
        Direccion = st.sidebar.text_input('Direccion:')
        fecha_actual = datetime.now()
        
        if st.sidebar.button("Agregar"):
            # Cargar el DataFrame existente
            df = cargar_df()

            # Validar que todos los campos estén completos
            if not Nombre_Cliente or not Contacto or not Telefono or not Email or not Direccion:
                st.sidebar.warning("Por favor completa todos los campos.")
            elif Nombre_Cliente.lower() in df['Nombre_Cliente'].str.lower().values:
                st.sidebar.warning("El Cliente ya existe. Por favor, elige otro nombre.")
            else:
                # Crear nueva fila con los datos del nuevo Cliente
                nueva_fila = pd.DataFrame({'Nombre_Cliente': [Nombre_Cliente],
                                        'Contacto': [Contacto],
                                        'Telefono': [Telefono],
                                        'Email': [Email],
                                        'Direccion': [Direccion],
                                        'Fecha': [fecha_actual]})
                
                # Concatenar el DataFrame original con el nuevo DataFrame
                df = pd.concat([df, nueva_fila], ignore_index=True)

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Agregado"
                indice_modificado = df.shape[0] - 1  # Índice de la fila recién agregada

    elif accion == "Modificar Cliente":
        st.sidebar.title("Modificar Cliente")
        opciones = df['Nombre_Cliente'].tolist()
        Cliente_modificar = st.sidebar.selectbox("Selecciona un Cliente:", opciones)

        if Cliente_modificar:
            indice_modificar = df[df['Nombre_Cliente'] == Cliente_modificar].index[0]
            Telefono = st.sidebar.text_input('Telefono:', value=df.loc[indice_modificar, 'Telefono'])
            Contacto = st.sidebar.text_input('Contacto:', value=df.loc[indice_modificar, 'Contacto'])
            Email = st.sidebar.text_input('Email:', value=df.loc[indice_modificar, 'Email'])
            Direccion = st.sidebar.text_input('Direccion:', value=df.loc[indice_modificar, 'Direccion'])
        
        if st.sidebar.button("Modificar"):
            # Validar que todos los campos estén completos
            if not Telefono or not Contacto or not Email or not Direccion:
                st.sidebar.warning("Por favor completa todos los campos.")
            else:
                # Actualizar los valores en el DataFrame
                df.loc[indice_modificar, 'Telefono'] = Telefono
                df.loc[indice_modificar, 'Contacto'] = Contacto
                df.loc[indice_modificar, 'Email'] = Email
                df.loc[indice_modificar, 'Direccion'] = Direccion

                # Guardar el DataFrame actualizado
                guardar_df(df)
                accion_realizada = "Modificado"
                indice_modificado = indice_modificar
    
     
            
    st.header("📝 Cliente agregado o modificado")
    # Mostrar la fila que se agregó o modificó
    if accion_realizada:
        st.sidebar.success(f"Se ha {accion_realizada} el Cliente:")
        st.dataframe(df.iloc[indice_modificado:indice_modificado+1])


##########################################################################

if selected == 'Ventas':    
    st.title(f'💰 Ventas') 
    st.markdown("""En esta página se muestra una tabla con los datos de las ventas existentes, la cual podrás observar a continuación 👇.

***👈 Puedes acceder en la barra lateral*** para agregar nuevas ventas o eliminar las ventas existentes. Selecciona la acción que deseas realizar en el menú desplegable de 'Gestión de ventas'.

Una vez elegida la opción deseada, aparecerán a continuación menús desplegables o campos para rellenar. Puedes agregar  el nombre del producto, en el menu despleglable y luego rellenar los campos.  Para eliminar una venta, selecciona el numero de indice correspondiente. Una vez que hayas completado los campos, presiona el botón 'Agregar' o 'Modificar'.

¡No te olvides de completar todos los campos! 💪""")

    # Separar el último encabezado del resto del contenido con una línea horizontal
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header(f'📅 Tabla de Ventas')

    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df(nombre_archivo):
        try:
            df = pd.read_csv(nombre_archivo)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre_Producto', 'Cantidad', 'Precio_Venta', 'Total', 'Nombre_Cliente', 'Fecha'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df, nombre_archivo):
        df.to_csv(nombre_archivo, index=False)

    # Cargar el DataFrame de productos y clientes
    df_productos = cargar_df("Productos.csv")
    df_clientes = cargar_df("Clientes.csv")

    # Inicializar el DataFrame de ventas
    df_ventas = cargar_df("Ventas.csv")

    # Sidebar para agregar o eliminar ventas
    st.sidebar.title("Gestión de Ventas")
    accion = st.sidebar.selectbox("Seleccione una acción", ["Agregar Venta", "Eliminar Venta"])

    # Separar las opciones con una línea horizontal
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    if accion == "Agregar Venta":
        # Sidebar para agregar ventas
        st.sidebar.title("Agregar Venta")
        producto_elegido = st.sidebar.selectbox("Selecciona un Producto:", df_productos['Nombre_Producto'].tolist())
        cantidad = st.sidebar.number_input('Cantidad:', min_value=1, step=1)
        precio_venta = st.sidebar.number_input('Precio de Venta:', format="%.2f")
        nombre_cliente = st.sidebar.selectbox("Selecciona un Cliente:", df_clientes['Nombre_Cliente'].tolist())
        
        # Validar que ningún campo esté vacío
        if st.sidebar.button("Agregar"):
            if not producto_elegido or not cantidad or precio_venta is None or not nombre_cliente:
                st.sidebar.warning("Por favor completa todos los campos.")
            else:
                # Calcular el total de la venta
                total_venta = cantidad * precio_venta

                # Crear una nueva fila con los datos de la venta
                nueva_venta = pd.DataFrame({
                    'Nombre_Producto': [producto_elegido],
                    'Cantidad': [cantidad],
                    'Precio_Venta': [precio_venta],
                    'Total': [total_venta],
                    'Nombre_Cliente': [nombre_cliente],
                    'Fecha': [datetime.now()]  # Guardar la fecha actual
                })

                # Concatenar el DataFrame original con la nueva venta
                df_ventas = pd.concat([df_ventas, nueva_venta], ignore_index=True)

                # Guardar el DataFrame actualizado
                guardar_df(df_ventas, "Ventas.csv")

                # Mostrar mensaje de éxito
                st.sidebar.success("Venta agregada correctamente.")

    elif accion == "Eliminar Venta":
        # Sidebar para eliminar ventas
        st.sidebar.title("Eliminar Venta")

        # Obtener la lista de índices de las ventas existentes para seleccionar la venta a eliminar
        ventas_exist = df_ventas.index.tolist()
        venta_a_eliminar = st.sidebar.selectbox("Selecciona una Venta para Eliminar:", ventas_exist)

        # Validar si se seleccionó una venta para eliminar
        if venta_a_eliminar is not None:
            # Mostrar los detalles de la venta seleccionada
            st.sidebar.write("Detalles de la Venta Seleccionada:")
            st.sidebar.write(df_ventas.iloc[venta_a_eliminar])

            # Botón para confirmar la eliminación de la venta seleccionada
            if st.sidebar.button("Eliminar Venta"):
                # Guardar la venta eliminada para mostrarla después
                venta_eliminada = df_ventas.iloc[venta_a_eliminar]

                # Eliminar la venta del DataFrame
                df_ventas.drop(index=venta_a_eliminar, inplace=True)

                # Reiniciar el índice
                df_ventas.reset_index(drop=True, inplace=True)

                # Guardar el DataFrame actualizado
                guardar_df(df_ventas, "Ventas.csv")

                # Mostrar mensaje de éxito
                st.sidebar.success("Venta eliminada correctamente.")

    # Calcular el total de cantidades y el total de ventas
    total_cantidades = df_ventas['Cantidad'].sum()
    total_ventas = df_ventas['Total'].sum()

    # Mostrar el total de cantidades y el total de ventas
    st.write(f"**Total de Cantidades:** {total_cantidades}")
    st.write(f"**Total de Ventas:** {total_ventas}")

    # Mostrar el DataFrame actualizado de ventas
    st.dataframe(df_ventas)





################################################################################################


if selected == 'Egresos':    
    st.title(f'💸 Egresos') 
    st.markdown("""En esta página se muestra una tabla con los datos de los egresos existentes, la cual podrás observar a continuación 👇.

***👈 Puedes acceder en la barra lateral*** para agregar nuevos egresos o crear los egresos existentes. Selecciona la acción que deseas realizar en el menú desplegable de 'Gestión de egresos'.

Una vez elegida la opción deseada, aparecerán a continuación menús desplegables o campos para rellenar. Puedes agregar o modificar el nombre del proveedor, el contacto, el teléfono, el correo electrónico y la dirección. Una vez que hayas completado los campos, presiona el botón 'Agregar importe' o 'Actualizar importe' .

¡No te olvides de completar todos los campos! 💪""")

    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df(nombre_archivo):
        try:
            df = pd.read_csv(nombre_archivo)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nombre', 'Direccion', 'Contacto', 'Telefono', 'Importe', 'Descripcion', 'Fecha'])
        return df

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df, nombre_archivo):
        df.to_csv(nombre_archivo, index=False)

    # Cargar el DataFrame de egresos creados
    df_egresos_creados = cargar_df("Egresos_Creados.csv")

    # Cargar el DataFrame de egresos agregados
    df_egresos_agregados = cargar_df("Egresos_Agregados.csv")

    # Mostrar la tabla de egresos creados
    st.title("📅 Tabla de Egresos Creados")
    st.dataframe(df_egresos_creados)
    st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal

    # Mostrar la tabla de egresos agregados
    st.title("📝 Tabla de Egresos Agregados")
    st.dataframe(df_egresos_agregados)
    
    # Calcular el total de egresos agregados
    total_egresos_agregados = df_egresos_agregados['Importe'].sum()
    st.write(f"**Total de Egresos Agregados:** {total_egresos_agregados}")
    st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal

    # Sidebar para elegir la opción
    opcion = st.sidebar.selectbox("Seleccionar Opción", ("Seleccionar Opción", "Crear Egreso", "Agregar Egreso"))

    if opcion == "Crear Egreso":
        st.title("📁 Crear Egreso")
        nombre = st.sidebar.text_input("Nombre")
        direccion = st.sidebar.text_input("Dirección")
        contacto = st.sidebar.text_input("Contacto")
        telefono = st.sidebar.text_input("Teléfono")
        importe = st.sidebar.number_input("Importe", step=0.01, format="%.2f")
        descripcion = st.sidebar.text_area("Descripción")
        
        if st.sidebar.button("Agregar Egreso"):
            # Validar que todos los campos estén completos
            if not nombre or not direccion or not contacto or not telefono or importe is None or not descripcion:
                st.sidebar.warning("Por favor completa todos los campos.")
            else:
                # Verificar si el egreso ya existe en la tabla de egresos creados
                if nombre in df_egresos_creados['Nombre'].values:
                    st.sidebar.warning("Ya existe un egreso con ese nombre.")
                else:
                    nuevo_egreso = pd.DataFrame({
                        'Nombre': [nombre],
                        'Direccion': [direccion],
                        'Contacto': [contacto],
                        'Telefono': [telefono],
                        'Importe': [importe],
                        'Descripcion': [descripcion],
                        'Fecha': [datetime.now()]  # Guardar la fecha actual
                    })
                    df_egresos_creados = pd.concat([df_egresos_creados, nuevo_egreso], ignore_index=True)
                    guardar_df(df_egresos_creados, "Egresos_Creados.csv")
                    st.sidebar.success("Egreso creado correctamente.")

                    # Mostrar el egreso agregado debajo de la tabla
                    st.header("Egreso Agregado")
                    st.write(nuevo_egreso)

    elif opcion == "Agregar Egreso":
        st.title("📁 Agregar Egreso")
        opciones_egresos = df_egresos_creados['Nombre'].tolist()
        egreso_seleccionado = st.sidebar.selectbox("Seleccionar Egreso Existente", opciones_egresos)
        
        if egreso_seleccionado:
            # Mostrar detalles del egreso seleccionado
            egreso_detalle = df_egresos_creados[df_egresos_creados['Nombre'] == egreso_seleccionado]
            # st.sidebar.write("Detalles del Egreso:")
            # st.sidebar.write(egreso_detalle)

            # Agregar importe float en la barra lateral
            nuevo_importe = st.sidebar.number_input("Nuevo Importe", step=0.01, format="%.2f")

            if st.sidebar.button("Actualizar Importe"):
                # Validar que el importe no esté vacío
                if nuevo_importe is None:
                    st.sidebar.warning("Por favor ingresa un valor para el importe.")
                else:
                    # Actualizar el importe del egreso seleccionado en la tabla de egresos agregados
                    nuevo_egreso_agregado = pd.DataFrame({
                        'Nombre': [egreso_seleccionado],
                        'Direccion': egreso_detalle['Direccion'].values[0],  # Obtener el valor único del egreso seleccionado
                        'Contacto': egreso_detalle['Contacto'].values[0],    # Obtener el valor único del egreso seleccionado
                        'Telefono': egreso_detalle['Telefono'].values[0],    # Obtener el valor único del egreso seleccionado
                        'Importe': [nuevo_importe],
                        'Descripcion': egreso_detalle['Descripcion'].values[0]  # Obtener el valor único del egreso seleccionado
                    })
                    df_egresos_agregados = pd.concat([df_egresos_agregados, nuevo_egreso_agregado], ignore_index=True)
                    guardar_df(df_egresos_agregados, "Egresos_Agregados.csv")
                    st.sidebar.success("Egreso agregado correctamente.")

                    # Actualizar el importe del egreso seleccionado en la tabla de egresos creados
                    df_egresos_creados.loc[df_egresos_creados['Nombre'] == egreso_seleccionado, 'Importe'] = nuevo_importe
                    guardar_df(df_egresos_creados, "Egresos_Creados.csv")

                    # Mostrar el producto modificado debajo de la tabla
                    st.header("Producto Modificado")
                    st.write(egreso_detalle)



######################################################################################################    

if selected == 'Visualizacion':
    st.title(f'👁 Visualizacion') 
    st.markdown("""
## Dashboard de Operaciones

En esta página, encontrarás gráficos que te permitirán visualizar de manera más simplificada los datos de tus operaciones.

**👈 Puedes acceder en la barra lateral** para filtrar el nombre de los productos y el nombre de los clientes en un menú desplegable de opciones múltiples.

Una vez seleccionadas las opciones deseadas, se mostrará una tabla con el total de los productos y un resumen de las ventas totales, así como el total de todos los productos vendidos. Debajo de esta tabla, encontrarás un gráfico de barras que muestra el total vendido por cada producto.

Además, se incluye un gráfico de torta que muestra el porcentaje de los productos más vendidos, acompañado de una tabla numérica para una mejor comprensión. Por último, se presenta un gráfico de barras que representa el total de ventas por cliente.

¡No olvides completar todos los campos para obtener una visualización completa de tus datos!
""")
    st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal
    

    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df(nombre_archivo):
        try:
            df = pd.read_csv(nombre_archivo)
        except FileNotFoundError:
            df = pd.DataFrame()  # DataFrame vacío si el archivo no existe
        return df

    # Cargar el DataFrame de Ventas
    df_ventas = cargar_df("Ventas.csv")

    # Calcular el total de ventas
    total_ventas = df_ventas['Total'].sum() if not df_ventas.empty else 0

    

    st.sidebar.header('Filtrar por Nombre de Producto y Cliente')

    # Filtrar por Nombre_producto y Nombre_Cliente
    nombres_productos = df_ventas['Nombre_Producto'].unique()
    nombres_clientes = df_ventas['Nombre_Cliente'].unique()

    filtro_nombre_producto = st.sidebar.multiselect('Seleccionar Nombre de Producto', nombres_productos, default=nombres_productos)
    filtro_nombre_cliente = st.sidebar.multiselect('Seleccionar Nombre de Cliente', nombres_clientes, default=nombres_clientes)

    # Aplicar filtros al DataFrame de ventas
    df_filtrado_barras = df_ventas[df_ventas['Nombre_Producto'].isin(filtro_nombre_producto) & df_ventas['Nombre_Cliente'].isin(filtro_nombre_cliente)]
    df_filtrado_tabla = df_ventas[df_ventas['Nombre_Producto'].isin(filtro_nombre_producto) & df_ventas['Nombre_Cliente'].isin(filtro_nombre_cliente)]

    # Mostrar el DataFrame filtrado
    st.header('📅 DataFrame Filtrado')
    st.write(df_filtrado_tabla)
    
    st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal
    
    # Calcular la suma de la columna "Total" y la cantidad de productos para el DataFrame de tabla
    total_ventas_filtrado_tabla = df_filtrado_tabla['Total'].sum() if not df_filtrado_tabla.empty else 0
    cantidad_productos_tabla = len(df_filtrado_tabla)

    st.header('📋 Resumen de Ventas Filtradas (Tabla)')
    st.write(f"Total de Ventas Filtradas (Tabla): ${total_ventas_filtrado_tabla}")
    st.write(f"Cantidad de Productos (Tabla): {cantidad_productos_tabla}")

    st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal
    
    # Gráfico de barras de Total de Ventas por Producto
    st.subheader('📈 Total de Ventas por Producto')
    chart_productos = alt.Chart(df_filtrado_barras).mark_bar().encode(
        x='Nombre_Producto',
        y='sum(Total)',
        tooltip=['Nombre_Producto', 'sum(Total)']
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(chart_productos, use_container_width=True)

    # Cargar los datos de ventas desde el archivo CSV (ya lo has hecho previamente)
    df_ventas = cargar_df("Ventas.csv")

    # Calcular el porcentaje de productos por cantidad
    porcentaje_productos = df_ventas['Nombre_Producto'].value_counts(normalize=True) * 100
    total_productos = df_ventas['Nombre_Producto'].value_counts()

    # Crear un DataFrame con la información
    df_productos_info = pd.DataFrame({'Porcentaje (%)': porcentaje_productos, 'Total': total_productos})

    # Mostrar la tabla
    st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal
    st.subheader('🍰 Porcentaje y Total de Productos por Cantidad')
    st.write(df_productos_info)

    # Crear el gráfico de torta
    fig, ax = plt.subplots()
    ax.pie(porcentaje_productos, labels=porcentaje_productos.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    
    
    st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal
    # Gráfico de barras de Total de Ventas por Cliente
    st.subheader('📈 Total de Ventas por Cliente')
    chart_clientes = alt.Chart(df_filtrado_barras).mark_bar().encode(
        x='Nombre_Cliente',
        y='sum(Total)',
        tooltip=['Nombre_Cliente', 'sum(Total)']
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(chart_clientes, use_container_width=True)

    

#####################################################################################################

# df = pd.read_csv("Ventas.csv")
# pr = df.profile_report()

# st_profile_report(pr)





