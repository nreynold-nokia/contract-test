import { Item } from './api-types'
import './App.css'

function App() {
  const myItem: Item = { name: 'nolan', id: 1, color: 'green' }

  return (
    <>
      <h1>Test types</h1>
      <div className="card">
        name {myItem.name}
        id {myItem.id}
        color {myItem.color}
      </div>
    </>
  )
}

export default App
