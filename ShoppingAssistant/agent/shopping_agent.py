from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from tools.product_tools import search_product, recommend_products
from tools.cart_tools import add_to_cart, view_cart, remove_from_cart
from tools.order_tools import check_order_status

llm = Ollama(model="llama2-7b")

prompt_template = """
You are an intelligent shopping assistant. 
User query: {query}
Provide the best possible response based on the user's input.
Your capabilities include:
1. Product search
2. Product recommendations
3. Cart management (add, remove, view)
4. Order status checks
"""

prompt = PromptTemplate(input_variables=["query"], template=prompt_template)
agent = LLMChain(llm=llm, prompt=prompt)

def process_user_input(query):
    if "add to cart" in query:
        parts = query.split()
        try:
            product_id = int(parts[-2])
            quantity = int(parts[-1])
            return add_to_cart(product_id, quantity)
        except ValueError:
            return "Invalid product ID or quantity."
    elif "remove from cart" in query:
        try:
            product_id = int(query.split()[-1])
            return remove_from_cart(product_id)
        except ValueError:
            return "Invalid product ID."
    elif "view cart" in query:
        return view_cart()
    elif "order status" in query:
        order_id = query.split()[-1]
        return check_order_status(order_id)
    else:
        return agent.run({"query": query})
