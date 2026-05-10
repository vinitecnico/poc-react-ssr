import { Product } from "@/types/product";

async function getProducts() {
  const response = await fetch(
    "http://localhost:3000/api/products",
    {
      cache: "no-store",
    }
  );

  return response.json();
}



export default async function Home() {
  const data = await getProducts();

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold mb-6">
        Produtos SSR
      </h1>

      <div className="grid gap-4">
        {data.products?.map((product: Product) => (
          <div
            key={product.id}
            className="border p-4 rounded"
          >
            <h2 className="font-bold">
              {product.name}
            </h2>

            <p>
              R$ {product.price}
            </p>
          </div>
        ))}
      </div>
    </main>
  );
}