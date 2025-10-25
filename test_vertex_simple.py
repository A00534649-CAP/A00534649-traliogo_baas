#!/usr/bin/env python3
"""
Test simple para verificar conectividad con Vertex AI
"""
import os

def main():
    print("🔍 Verificando configuración de Vertex AI...")
    
    project = os.getenv("GCLOUD_PROJECT", "trailogo-dev")
    location = os.getenv("VERTEX_LOCATION", "us-central1")
    
    print(f"   Project: {project}")
    print(f"   Location: {location}")
    print(f"   Credentials: {os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'No configuradas')}")
    
    try:
        from google.cloud import aiplatform
        
        # Solo inicializar, no usar modelos
        aiplatform.init(project=project, location=location)
        print("✅ Vertex AI API accessible")
        
        # Verificar si podemos listar algo básico
        print("📋 Intentando listar datasets...")
        datasets = aiplatform.Dataset.list(limit=1)
        print(f"✅ Conexión exitosa a Vertex AI")
        
    except Exception as e:
        if "API has not been used" in str(e):
            print("❌ Vertex AI API no habilitada")
            print("   Habilítala en: https://console.cloud.google.com/marketplace/product/google/aiplatform.googleapis.com")
        elif "permission" in str(e).lower():
            print("❌ Falta permisos para Vertex AI")
            print("   Agrega rol 'Vertex AI User' a tu cuenta de servicio")
        else:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()