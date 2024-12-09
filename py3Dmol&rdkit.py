from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

# Lista de moléculas con sus cadenas SMILES
moleculas = {
    "Agua": "O",
    "Etanol": "CCO",
    "Ciclohexano": "C1CCCCC1",
    "Ácido acético": "CC(=O)O",
    "Benceno": "C1=CC=CC=C1",
    "Metano": "C",
    "Metanol": "CO",
    "Etano": "CC",
    "Propano": "CCC",
    "Butano": "CCCC"
}

# Función para generar el modelo 3D
def generar_modelo_3D(smiles, titulo):
    mol = Chem.MolFromSmiles(smiles)  # Crear la molécula desde SMILES
    if mol is None:
        print(f"Error al crear la molécula desde SMILES: {smiles}")
        return None  # Manejo de errores si SMILES es inválido

    mol = Chem.AddHs(mol)  # Agregar hidrógenos implícitos
    AllChem.EmbedMolecule(mol)  # Generar las coordenadas 3D
    AllChem.MMFFOptimizeMolecule(mol)  # Optimizar la geometría

    # Generar la vista en py3Dmol
    mb = Chem.MolToMolBlock(mol)
    view = py3Dmol.view(width=400, height=400)
    view.addModel(mb, "mol")
    view.setStyle({"stick": {}})
    view.setBackgroundColor("white")
    view.zoomTo()
    print(f"Modelo 3D generado: {titulo}")
    return view

# Mostrar los modelos de las moléculas
for nombre, smiles in moleculas.items():
    print(f"Generando modelo para: {nombre}")
    modelo = generar_modelo_3D(smiles, nombre)
    if modelo:  # Verificar que el modelo se generó correctamente
        modelo.show()
        