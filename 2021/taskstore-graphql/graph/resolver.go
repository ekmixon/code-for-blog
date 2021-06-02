package graph

import "example.com/internal/taskstore"

// This file will not be regenerated automatically.
//
// It serves as dependency injection for your app, add any dependencies you require here.

type Resolver struct {
	store *taskstore.TaskStore
}
