from src.graph import graph


print("=" * 60)
print("🤖 AI Engineering Knowledge Assistant")
print("LangGraph Version")
print("=" * 60)


while True:

    question = input("\n👤 Tú: ")

    if question.lower() == "salir":
        break


    print("\n🚀 Ejecutando LangGraph...")


    try:

        result = graph.invoke(
            {
                "question": question,
                "context": "",
                "answer": ""
            }
        )


        print("\n========== RESULTADO ==========")

        print(result)

        print("================================")


        print(
            f"\n🤖\n{result.get('answer')}"
        )


    except Exception as e:

        print("\n❌ ERROR:")
        print(e)