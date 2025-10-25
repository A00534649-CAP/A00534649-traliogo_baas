#!/usr/bin/env python3
"""
Script que espera hasta que Vertex AI esté funcionando
"""
import time
import os
from dotenv import load_dotenv

def test_vertex():
    try:
        load_dotenv()
        import vertexai
        from vertexai.generative_models import GenerativeModel
        
        project_id = os.getenv('GCLOUD_PROJECT')
        location = os.getenv('VERTEX_LOCATION')
        model_name = os.getenv('VERTEX_MODEL')
        
        vertexai.init(project=project_id, location=location)
        model = GenerativeModel(model_name)
        
        response = model.generate_content("Di solo: OK")
        return True, response.text.strip()
        
    except Exception as e:
        return False, str(e)

def main():
    print("⏳ Esperando a que se propaguen los permisos de Vertex AI...")
    print("   (Esto puede tomar 1-5 minutos)")
    
    for attempt in range(1, 11):  # Intentar 10 veces
        print(f"\n🔄 Intento {attempt}/10...")
        
        success, result = test_vertex()
        
        if success:
            print(f"🎉 ¡Vertex AI funciona!")
            print(f"   Respuesta: {result}")
            print("\n✅ Gemini está listo para usar!")
            return True
        else:
            if "403" in result and "permission" in result.lower():
                print("   ❌ Permisos aún propagándose...")
            else:
                print(f"   ❌ Error: {result[:100]}...")
            
            if attempt < 10:
                print("   ⏱️ Esperando 30 segundos...")
                time.sleep(30)
    
    print("\n⚠️ Los permisos tardan más de lo esperado.")
    print("   Verifica en Google Cloud Console que el rol 'Vertex AI User' esté asignado.")
    return False

if __name__ == "__main__":
    main()