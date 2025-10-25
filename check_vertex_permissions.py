#!/usr/bin/env python3
"""
Script para verificar si los permisos de Vertex AI están configurados correctamente
"""
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    
    project_id = os.getenv('GCLOUD_PROJECT')
    location = os.getenv('VERTEX_LOCATION') 
    model_name = os.getenv('VERTEX_MODEL')
    
    print("🔍 Verificando permisos de Vertex AI...")
    print(f"   Project: {project_id}")
    print(f"   Model: {model_name}")
    
    try:
        import vertexai
        from vertexai.generative_models import GenerativeModel
        
        # Inicializar
        vertexai.init(project=project_id, location=location)
        
        # Cargar modelo
        model = GenerativeModel(model_name)
        print("✅ Modelo cargado exitosamente")
        
        # Probar generación simple
        response = model.generate_content(
            "Responde solo: OK", 
            generation_config={'max_output_tokens': 5}
        )
        
        print(f"✅ Vertex AI funciona! Respuesta: {response.text.strip()}")
        print("🎉 Gemini está listo para usar")
        
        return True
        
    except Exception as e:
        error_str = str(e)
        if '403' in error_str and 'permission' in error_str.lower():
            print("❌ Falta permiso 'Vertex AI User'")
            print(f"   Agregar en: https://console.cloud.google.com/iam-admin/iam?project={project_id}")
            print(f"   Cuenta: id-firebase-admin-api@{project_id}.iam.gserviceaccount.com")
        else:
            print(f"❌ Error: {error_str}")
        return False

if __name__ == "__main__":
    main()