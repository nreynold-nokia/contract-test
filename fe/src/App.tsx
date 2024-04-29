import { Item } from './api-types'
import './App.css'

function App() {
  const myItem: Item = { name: 'nolan', id: 1 }

  return (
    <>
      <h1>Test types</h1>
      <div className="card">
        name {myItem.name}
        id {myItem.id}
      </div>
    </>
  )
}

export default App
